import re
from selenium import webdriver
browser = webdriver.Edge()
browser.get('http://finance.sina.com.cn/realstock/company/sh600519/nc.shtml')
data = browser.page_source
browser.quit()
p_price = '<div id="price" class=".*?">(.*?)</div>'
price = re.findall(p_price, data)
print(price)
