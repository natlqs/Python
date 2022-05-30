from selenium import webdriver
import re
import requests
browser = webdriver.Edge()
url = 'https://data.eastmoney.com/report/zw_stock.jshtml?infocode=AP202108241512140374'
browser.get(url)
data = browser.page_source
print(data)