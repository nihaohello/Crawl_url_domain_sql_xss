#coding=utf-8
import re
from urllib.parse import urlparse
from urllib import parse
import sys
if len(sys.argv) != 2:
    print("python Get_url.py urls.txt")
    exit()
name=sys.argv[1]
def select_str(name):
    urls=[]
    f = open(name, encoding="utf-8")
    for i in f.readlines():
        if ".do" in i:
            i = i.rstrip("\n  ")
            # print(i)
            j = re.findall("http.*", i)[0]
            j=parse.unquote(j)
            urls.append(j)
    f.close()
    return urls

a=input("输入url包含的字符:")
urls=select_str(name)
with open("urls_results.txt","w+",encoding="utf-8") as f:
    for url in urls:
        if a in url:
            #print(url)
            f.write(url)
            f.write("\n")
f.close()
print("得到的url在urls_results.txt文件中。")