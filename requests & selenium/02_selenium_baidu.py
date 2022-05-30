import time
from selenium import webdriver

browser = webdriver.Edge()

browser.get('https://baidu.com')

time.sleep(10)
browser.quit