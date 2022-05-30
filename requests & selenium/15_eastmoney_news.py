from selenium import webdriver
import re

edge_options = webdriver.EdgeOptions()
edge_options.add_argument('--headless')

def dongfang(company):
    browser = webdriver.Edge(options=edge_options)
    url = 'https://so.eastmoney.com/news/s?keyword=' + company
    browser.get(url)
    data = browser.page_source
    browser.quit()
    p_title = '<div class="news_item_t"><a href=".*?" target="_blank">(.*?)</a></div>'
    p_href = '<div class="news_item_t"><a href="(.*?)" target="_blank">.*?</a></div>'
    p_date = '<span class="news_item_time">(.*?)</span>'
    title = re.findall(p_title, data)
    href = re.findall(p_href, data)
    date = re.findall(p_date, data) # 提取的日期可能包括换行，添加re.S来自动考虑换行的影响
    for i in range(len(title)):
        title[i] = re.sub('<.*?>', '', title[i])
        date[i] = date[i].split(' ')[0]
        print(str(i+1) + '.' + title[i] + ' - ' + date[i])
        print(href[i])
    
companies = ['格力电器', '阿里巴巴', '腾讯', '京东']
for i in companies:
    try:
        dongfang(i)
        print(i + ': 该公司东方财富网爬取成功')
    except:
        print(i + ': 该公司东方财富爬取失败')