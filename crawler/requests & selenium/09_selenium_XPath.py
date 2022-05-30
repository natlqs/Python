# 打开浏览器，输入网址，输入搜索词，enter，关闭
# selenium Xpath选择器
from selenium import webdriver  # 导入Selenium库中的webdriver功能
import time
browser = webdriver.Edge()  # 声明要模拟的浏览器是edge
browser.maximize_window()   # 将模拟浏览器窗口最大化
browser.get('https://www.baidu.com/')   # 在模拟浏览器中打开指定网址
browser.find_element_by_xpath('//*[@id="kw"]').send_keys('python')
browser.find_element_by_xpath('//*[@id="su"]').click()
time.sleep(2)
browser.quit()  # 关闭模拟浏览器