from selenium import webdriver
import re
import pandas as pd
import time

browser = webdriver.Edge()
browser.get('https://data.eastmoney.com/report/stock.jshtml')
data = browser.page_source
table = pd.read_html(data)[1]
p_href = '<td><a href="/report/info/(.*?)"'
href = re.findall(p_href, data)
for i in range(len(href)):
    href[i] = "https://data.eastmoney.com/report/info/" + href[i]
table['网址'] = href
table = table.astype('str')
for i, row in table.iterrows():
    print(str(i+1) + '.' + row['股票简称']['股票简称'])
    print('研究日期：' + row['日期']['日期'])
    print('研报标题: ' + row['报告名称']['报告名称'])
    print('公司评级: ' + row['东财评级']['东财评级'])
    print('评级变化: ' + row['评级变动']['评级变动'])
    print('近一个月个股研报数：' + row['近一月个股研报数']['近一月个股研报数'])
    print('研报链接: ' + href[i])
    print('-' *20)
