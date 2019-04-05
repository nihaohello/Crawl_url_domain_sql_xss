#coding=utf-8
import re
from urllib.parse import urlparse
from urllib import parse
import sys
def select_str(file_name):
    urls=[]
    f = open(file_name, encoding="utf-8")
    for i in f.readlines():
        if ".do" in i:
            i = i.rstrip("\n  ")
            # print(i)
            j = re.findall("http.*", i)[0]
            j=parse.unquote(j)
            urls.append(j)
    f.close()
    return urls
if len(sys.argv) != 2:
    print("python Get_url.py urls.txt")
    exit()
name=sys.argv[1]
urls=select_str(name)
urls=list(set(urls))
print(len((urls)))
#sql_xss.txt
with open("sql_xss漏洞.txt","w+",encoding="utf-8") as f:
    for url in urls:
        if "?" in url and "=" in url:
            f.write(url)
            f.write("\n")
f.close()
#stru
with open("struts2漏洞.txt","w+",encoding="utf-8") as f:
    for url in urls:
        if ".do" in url and ".active" in url:
            f.write(urls)
            f.write("\n")
f.close()
#
domains=[]
for url in urls:
    a = urlparse(url)[1]
    if a not in domains:
        domains.append(a)
with open("域名domain.txt","w+",encoding="utf-8") as f:
    for domain in domains:
        f.write(domain)
        f.write("\n")
f.close()

with open("文件包含.txt","w+",encoding="utf-8") as f:
    for url in urls:
        if "file" in url:
            f.write()
            f.write("\n")
f.close()

with open("后台和配置.txt","w+",encoding="utf-8") as f:
    for url in urls:
        if "admin" in url or "login" in url or "Admin" in url or "Login" in url or "conf" in url:
            f.write(url)
            f.write("\n")
f.close()

'''
a="conf cnf xml conf reg inf rdp cfg txt ora ini sql dbf mdb log bkf bkp bak old backup upload"
b=a.split(" ")
for i in b:
    print("and \""+i+"\" in url",end=" ")
'''
with open("其他地址.txt","w+",encoding="utf-8") as f:
    for url in urls:
        if "xml" in url and "conf" in url and "cnf" in url and "xml" in url and "conf" in url and "reg" in url and "inf" in url and "rdp" in url and "cfg" in url and "txt" in url and "ora" in url and "ini" in url and "sql" in url and "dbf" in url and "mdb" in url and "log" in url and "bkf" in url and "bkp" in url and "bak" in url and "old" in url and "backup" in url and "upload" in url:
            f.write(url)
            f.write("\n")
f.close()

