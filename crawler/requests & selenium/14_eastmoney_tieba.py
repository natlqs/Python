from turtle import title
from selenium import webdriver
import re
edge_options = webdriver.EdgeOptions()
edge_options.add_argument('--headless')
browser = webdriver.Edge(options=edge_options)
browser.get('https://guba.eastmoney.com/list,600519.html')
data = browser.page_source
p_title = '<a href=".*?" title="(.*?)"'
title = re.findall(p_title, data)
for i in range(len(title)):
    print(str(i + 1) + '.' + title[i])