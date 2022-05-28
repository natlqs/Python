# 获取阿甘正传的豆瓣评分、简介。。。

import requests
import re
url = 'https://movie.douban.com/subject/1292720/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76'}
res = requests.get(url, headers = headers).text
titles = []
title1 = '"v:itemreviewed">(.*?)</span>'
year1 = '="year">(.*?)</span>'
score1 = '"v:average">(.*?)</strong>'
summary1 = '"v:summary"(.*?)</span>'
title = re.findall(title1, res, re.S)
year = re.findall(year1, res, re.S)
score = re.findall(score1, res, re.S)
summary = re.findall(summary1, res, re.S)
print(title, year, score, summary)
