1.  
功能：  
通过扫描网页链接（只匹配了href和src）扫描得到：  
（1）子域名：target_crawl_doamin.txt  
（2）sql_xss:target_crawl_sql_xss.txt  
（3）包含baidu.com的所有链接：target_crawl_urls.txt  
**（4）主要拿到url，处理都是小问题  
  
  
2.  
使用方法：  
python Crawl_url_domain_sql_xss.py domain.txt  
domain.txt  大概收集的子域名  
  
  
re.py是不加互斥锁，只加可重入锁的情况，只输出，效果更快点  
需要自己简单写个脚本处理下得到的所有url情况  
一般使用：  
python 1.py domain.txt | tee result.txt  
  
  
  
  
