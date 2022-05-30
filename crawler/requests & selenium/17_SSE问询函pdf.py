from selenium import webdriver
import time
import re
import requests

browser = webdriver.Edge()
url = 'http://www.sse.com.cn/disclosure/credibility/supervision/inquiries/'
browser.get(url)
'''
因为在请求查询页面时有一个加载的过程，所以必须在第4行代码让程序等待一定时间（这里为3秒）再继续运行，
否则用browser.page_source获取的网页源代码会不包含所需内容。
'''
time.sleep(3)   
data = browser.page_source
p_title = '<td><a href=".*?" target="_blank">(.*?)</a></td>'
p_href =  '<td><a href="(.*?)" target="_blank">.*?</a></td>'
title = re.findall(p_title, data)
href = re.findall(p_href, data)
for i in range(len(href)):
    res = requests.get(href[i])
    path = '.\\Python\\crawler\\requests & selenium\\SSEquery_pdf\\' + title[i] + '.pdf'
    try:
        file = open(path, 'wb')
        file.write(res.content)
        file.close()
        print('file saved')
    except:
        pass