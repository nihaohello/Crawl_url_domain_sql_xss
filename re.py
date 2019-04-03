# coding=utf-8
import requests
import re
from urllib.parse import urlparse
from urllib import parse
import sys
from concurrent.futures import ThreadPoolExecutor
import multiprocessing
import os
import vthread
import random
import threading
mutex1 = threading.RLock()
class crawl(object):
    def __init__(self, ur):
        self.url = url
        self.collect_url = []
        self.domain_collect_url=[]
        self.sql_xss_collect_url=[]
        self.file_name = "target_"
        self.num=random.randint(15,20)
    @vthread.pool(20)
    def run(self):
        b = self.deal_url(self.url)
        a = b[1].split(".")
        self.Is_url=a[1]+"."+a[2]
        #print(self.Is_url)
        num = 0
        self.crawl(self.url, num)
        #self.sql_xss_file_save()
        #self.file_domain_save()   #保存子域名的列表
    def crawl(self, url, num):
        #print(url)
        temp_urls=self.deal_url(url)
        try:
            temp_url=temp_urls[0]+"://"+temp_urls[1]
        except Exception:
            pass
        num = num + 1
        #print(num)
        if num <= self.num:
            try:
                s = requests.get(url=url,timeout=6)
                urls1 = re.findall('href=".*?"', s.text)
                urls2 = re.findall("href=\'.*?\'", s.text)
                urls3 = re.findall('src=".*?"', s.text)
                urls4 = re.findall("src=\'.*?\'", s.text)
                #urls=re.findall('.*?'+self.Is_url+".*?",s.text)
                urls = urls1 + urls2 + urls3 +urls4
                #print(urls)
                for i in urls:
                    if self.Is_url in i:
                        i = self.deal_href_src(i)
                        if "http" not in i:
                            i = "http://" + i
                        #print(i)
                    if self.Is_url not in i:
                        i=self.deal_href_src(i)
                        if "http" not in i:
                            i=temp_url+"/"+i
                    if "javascript" not in i and i not in self.collect_url:
                        if ((not i.endswith(".png")) and (not i.endswith("jpg")) and (not i.endswith("gif")) and (not i.endswith("css")) and (not i.endswith("js")) and (not i.endswith("ico"))):
                            if self.Is_url in i:
                                print(i)
                                mutex1.acquire()
                                self.collect_url.append(i)
                                mutex1.release()
                                '''j = self.deal_url(i)
                                j = j[1]
                                if j not in self.domain_collect_url:
                                    pass
                                    #self.domain_collect_url.append(j)
                                if (("=" in i) and (i not in self.sql_xss_collect_url) and ("?" in i)):
                                    pass
                                    #self.sql_xss_collect_url.append(i)
                                    '''
                                self.crawl(i, num)
                        # urls2=re.findall('src=".*?"',s.text)
                        # print(urls2)
            except Exception:
                pass
    def deal_url(self,url):
        return urlparse(url)
    def deal_href_src(self,i):
        i=parse.unquote(i)
        if "href=" in i:
            i = i.rstrip("\"").lstrip('href=')
            i = i.rstrip("\'").lstrip('href=')
            i = i.strip("\"")
            i = i.rstrip("/")
        if "src" in i:
            i = i.lstrip("src=").rstrip("\"")
            i = i.lstrip("\"")
            i = i.rstrip("/")
        i=i.replace("'","")
        i=i.strip(".").strip("/")
        return i
    def file_domain_save(self):
        print(self.domain_collect_url)
    def sql_xss_file_save(self):
        print(self.sql_xss_collect_url)
def qu_chong():
    dir_name = os.path.dirname(os.path.abspath(__file__))
    a = os.listdir(dir_name)
    for i in a:
        urls=[]
        if ".txt" in i:
            try:
                f = open(i, encoding="utf-8")
                for i in f.readlines():
                    urls.append(i.rstrip("\n"))
                urls = list(set(urls))
                f.close()
                with open(i, "w+", encoding="utf-8") as f:
                    for i in urls:
                        f.write(i)
                        f.write("\n")
                f.close()
            except Exception:
                pass

if len(sys.argv) != 2:
    print("python crawl.py domain.txt")
    exit()
file_name = sys.argv[1]
f=open(file_name,encoding="utf-8")

#删除存储url的文件，建议手动删除
'''
try:
    os.remove("target_crawl_doamin.txt")
except Exception:
    pass
try:
    os.remove("target_crawl_sql_xss.txt")
except Exception:
    pass
try:
    os.remove("target_crawl_urls.txt")
except Exception:
    pass
'''
#多进程
'''
pool=multiprocessing.Pool(multiprocessing.cpu_count())
for url in f.readlines():
    if not url.startswith("http"):
        url = "http://" + url
    url = url.rstrip("\n")
    pool.apply_async(crawl(url).run())
pool.close()
pool.join()
'''
#多线程
for url in f.readlines():
    if not url.startswith("http"):
        url = "http://" + url
    url = url.rstrip("\n")
    crawl(url).run()
#qu_chong()

