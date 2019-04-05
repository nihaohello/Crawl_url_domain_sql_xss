-------------------2019.4.4  
个人虽然在脚本中写了文件处理  
但实际，就是不用脚本处理文件，用tee命令（linux下，windows这个命令写文件极其影响速率）  
然后再写个脚本处理  
一.  
正在用的两个脚本:  
抓取总url的脚本.py  
抓取单个域名url的脚本.py  
使用：  
python 1.py domain.txt | tee result.txt  
  
  
二.  
紧跟增加的deal目录：  
#处理得到的urls  
1.自己的处理脚本.py:  
得到sql_xss，struts2，conf，admin，bak等url  
  
2.自行输入的脚本.py:  
输入字符，得到包含该字符的url  
  
  
三.处理命令  
linux下:  
sort -u result1.txt > result2.txt  
#shuf result2.txt  
#cat result2.txt | awk -F "]" '{print $2}' | tr -d " " > result3.txt  
cat result.txt | awk -F "]" '{print $2}' | awk -F " " '{print $1}'  >  result3.txt  
windows下:  
type final_urls.txt | find /v /c ""  
powershell:python 1.py domain.txt | tee result.txt  
  
