# 获取格隆汇头条及简介
import requests
import re
url = 'https://www.gelonghui.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76'}
try:
    res = requests.get(url, headers=headers).text
except Exception as e:
    print(e.args)
    print(str(e))
titles = []
# 提取網址和標題
headers1 = '<h2 data-v-f144bf8e>.*?</h2>'
summary0 = '<summary data-v-f144bf8e>.*?</summary>'
summary1 = re.findall(summary0, res, re.S)
headers2 = re.findall(headers1, res, re.S)
for i in range(len(headers2)):
    title = re.sub('</h2>', '', headers2[i])
    title = re.sub('<h2 data-v-f144bf8e>', '', title)
    summary = re.sub('</summary>', '', summary1[i])
    summary = re.sub('<summary data-v-f144bf8e>', '', summary)
    title = 'title: ' + title + '\n' + 'summary: ' + summary
    titles.append(title)
    print(title)
