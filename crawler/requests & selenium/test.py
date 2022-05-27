from selenium import webdriver
import time
import pandas as pd
import re
import requests

browser = webdriver.Edge()
url = 'http://www.sse.com.cn/disclosure/credibility/supervision/inquiries/'
browser.get(url)
data = browser.page_source
table = pd.read_html(data)[0]