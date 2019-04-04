一.  
功能：  
通过扫描网页链接（只匹配了href和src）扫描得到：  
（1）子域名：target_crawl_doamin.txt  
（2）sql_xss:target_crawl_sql_xss.txt  
（3）包含baidu.com的所有链接：target_crawl_urls.txt  
**（4）主要拿到url，处理都是小问题  
  
  
二.  
使用方法：  
python Crawl_url_domain_sql_xss.py domain.txt  
domain.txt  大概收集的子域名  
  
  
re.py是不加互斥锁，只加可重入锁的情况，只输出，效果更快点  
需要自己简单写个脚本处理下得到的所有url情况  
一般使用：  
python 1.py domain.txt | tee result.txt  
  
  
-------------------2019.4.4  
修改为re2.py  
三.反复比较了下，如果非要比较url和文件操作，由于锁的原因多线程的优势荡然无存  
个人暂时也没有找到高效的解决方法  
所以修改了下，就简单的输出就行了  
缺点（也是原先的功能）：  
1.url没有去重，会重复爬取url（深度自设）  
2.去掉文件处理  
  
python re2.py domain.txt | tee result.txt  
  
四.  
紧跟增加的deal目录：  
#处理得到的urls  
  
1.自己的处理脚本.py:  
得到sql_xss，struts2，conf，admin，bak等url  
  
2.自行输入的脚本.py:  
输入字符，得到包含该字符的url  
