from selenium import webdriver
import pandas as pd
import time
browser = webdriver.Edge()
url = 'https://www.jisilu.cn/data/cbnew/#cb'
browser.get(url)
time.sleep(2)
data = browser.page_source
time.sleep(2)
tables = pd.read_html(data)
df = tables[0]
df.to_excel('.\\Python\\crawler\\Pandas & Mysql\\可转债.xlsx')

