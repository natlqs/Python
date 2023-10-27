from selenium import webdriver
import time
edge_options = webdriver.EdgeOptions()
edge_options.add_argument('--headless')
browser = webdriver.Edge(options=edge_options)
browser.maximize_window()   # 将模拟浏览器最大化
browser.get('http://www.baidu.com')
browser.find_element_by_css_selector('#kw').send_keys('python')
browser.find_element_by_css_selector('#su').click()
time.sleep(2)
browser.quit()
