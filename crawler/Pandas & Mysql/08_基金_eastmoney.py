import pandas as pd
from selenium import webdriver
import time
import re

browser = webdriver.Edge()
browser.maximize_window()       # 将窗口最大化，以方便观察

url = 'https://fund.eastmoney.com/data/fundranking.html#tgp'
browser.get(url)
browser.find_element_by_xpath('//*[@id="showall"]').click()
time.sleep(3)
data = browser.page_source
table = pd.read_html(data)
df = table[3]
p_title_a = '<a href=".*?" title="(.*?)">.*?</a>'
p_title_b = '<a href=".*?" title=".*?">(.*?)</a>'
p_href = '<a href="(.*?)" title=".*?">.*?</a>'

title_a = re.findall(p_title_a, data)
title_b = re.findall(p_title_b, data)
href = re.findall(p_href, data)
for i in range(len(title_a)):
    href[i] = href[i].split('<a href="')[-1]
df['网址'] = href
df['基金名称'] = title_a
df.to_excel('.\\Python\\crawler\\Pandas & Mysql\\股票型基金.xlsx', index=False)