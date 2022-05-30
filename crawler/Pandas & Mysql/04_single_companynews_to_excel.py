import requests
import re
import pandas as pd


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50'}
url = 'https://www.baidu.com/s?rtt=4&tn=news&word=阿里巴巴'
res = requests.get(url, headers=headers).text
p_titie = '<a href=".*?" target="_blank" class="news-title-font_1xS-F" aria-label="标题：(.*?)" data-click="'
p_href = '<h3 class="news-title_1YtI1 "><a href="(.*?)" target="_blank" class="news-title-font_1xS-F'
title = re.findall(p_titie, res)
href = re.findall(p_href, res)
# print(title)
# print(href)
df = pd.DataFrame()
df['标题'] = title
df['网址'] = href
df.to_excel('.\\Python\\crawler\\Pandas & Mysql\\百度新闻-单家.xlsx', index=False)      # index = False 表示忽略行索引