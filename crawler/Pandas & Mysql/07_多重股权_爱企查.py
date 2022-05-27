from selenium import webdriver
import re
import time
import pandas as pd

# company_name = '中国华能集团有限公司'
def aiqicha(company_name):
    browser = webdriver.Edge()
    url = 'https://aiqicha.baidu.com/s?q=' + company_name
    browser.get(url)
    time.sleep(2)
    data = browser.page_source
    p_href = '" target="_blank" href="(.*?)"' # title="华能贵诚信托有限公司" data-log-an="company" data-log-idx="0"><em>华能</em>贵诚<em>信托</em>有限公司</a><span data-v-387da8b0="" class="tag blue">
    href = re.findall(p_href, data, re.S)
    url2 = 'https://aiqicha.baidu.com' + href[0]
    browser.get(url2)
    time.sleep(2)
    data = browser.page_source
    table  = pd.read_html(data)
    df = table[1]
    browser.quit()
    company = df['股东名称'][0]
    company_split = company.split(' ')
    print(company_split)
    for i in company_split:
        if len(i) > 6:
            print(i)
            return i

company = '贵州茅台'
while True:
    try:
        company = aiqicha(company)  # 获取company的控股股东并赋给company
        print(company)
    except:
        break   # break语句可以跳出for或while循环