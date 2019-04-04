# coding=utf-8
import requests
import re
from urllib.parse import urlparse
from urllib import parse
import sys
import os
import vthread
import random

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
                    if "javascript" not in i and "JavaScript" not in i:
                        if ((not i.endswith(".png")) and (not i.endswith("jpg")) and (not i.endswith("gif")) and (".css" not in i) and ((".js" not in i) or (".json" in i)) and (".ico" not in i)):
                            if self.Is_url in i:
                                print(i)
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

if len(sys.argv) != 2:
    print("python crawl.py domain.txt")
    exit()
file_name = sys.argv[1]
f=open(file_name,encoding="utf-8")
#多线程
for url in f.readlines():
    if not url.startswith("http"):
        url = "http://" + url
    url = url.rstrip("\n")
    crawl(url).run()


