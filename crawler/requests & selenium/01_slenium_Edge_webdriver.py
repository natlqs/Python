# 自动打开edge浏览器并打开指定网页
from lib2to3.pgen2 import driver
import time
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get('https://bing.com')

element = driver.find_element(By.ID, 'sb_form_q')
element.send_keys('WebDriver')
element.submit()

time.sleep(5)
driver.quit