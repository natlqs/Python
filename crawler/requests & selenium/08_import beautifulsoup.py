# 获取新浪新闻并用BS4解析
import requests
from bs4 import BeautifulSoup
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76'}

url = 'http://news.sina.com.cn/china/'
res = requests.get(url, headers = headers)
res.encoding = 'utf-8'      # 编码方式1，否则会乱码
res = res.text
# res = res.encode('ISO-8859-1').decode('utf-8')    #编码方式2，否则会乱码
# print(res)
soup = BeautifulSoup(res, 'html.parser')
a = soup.select('a')
for i in a:
    print(i.text)  