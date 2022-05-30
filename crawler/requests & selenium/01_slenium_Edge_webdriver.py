# 自动打开edge浏览器并打开指定网页
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get('https://bing.com')

element = driver.find_element(By.ID, 'sb_form_q')
element.send_keys('WebDriver')
element.submit()

time.sleep(5)
driver.quit