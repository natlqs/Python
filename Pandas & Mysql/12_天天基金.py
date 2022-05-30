from selenium import webdriver
import re
import time
import pandas as pd
from matplotlib import pyplot as plt



url = 'http://fundf10.eastmoney.com/jjjz_000001.html'
browser = webdriver.Edge()
browser.get(url)
time.sleep(2)
data = browser.page_source

table = pd.read_html(data)
df = table[3]
print(df)
pd.DataFrame.plot(df)
plt.show()