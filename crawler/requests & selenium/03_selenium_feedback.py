import time
from selenium import webdriver

browser = webdriver.Edge()
browser.get('https://www.gelonghui.com')

ata = browser.page_source
browser.quit()
# time.sleep(1)
print(ata)

