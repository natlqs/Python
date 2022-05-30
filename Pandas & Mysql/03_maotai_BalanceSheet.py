from selenium import webdriver
import pandas as pd


browser = webdriver.Edge()
url = 'https://vip.stock.finance.sina.com.cn/corp/go.php/vFD_BalanceSheet/stockid/600519/ctrl/part/displaytype/4.phtml'
browser.get(url)
data = browser.page_source

table= pd.read_html(data)

for i in range(len(table)):
    print(i)
    print(table[i])