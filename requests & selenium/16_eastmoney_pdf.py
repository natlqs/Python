from selenium import webdriver
import re
import requests

edge_options = webdriver.EdgeOptions()
edge_options.add_argument('--headless')
browser = webdriver.Edge(options=edge_options)
url = 'https://so.eastmoney.com/Yanbao/s?keyword=格力电器'
browser.get(url)
data = browser.page_source
p_href = '<div class="notice_item_t"><span class="notice_item_t_label">【<span>格力电器</span>】</span><a href="(.*?)" target="_blank">.*?</a></div>'
href = re.findall(p_href, data)
# print(href)
for i in range(len(href)):
    try:
        browser.get(href[i])
        datai= browser.page_source
        p_name = '<h1>(.*?)</h1>'
        p_href_pdf = '<a style="color: #039; text-decoration: underline; font-family: 宋体; font-size: 14px;" href="(.*?)">'
        name = re.findall(p_name, datai, re.S)
        name = re.sub('\s|\t|\n', '', name[0])
        href_pdf = re.findall(p_href_pdf, datai)
        res = requests.get(href_pdf[0])
        path = '.\\Python\\crawler\\requests & selenium\\eastmoney_pdf\\' + name + '.pdf'
        file = open(path, 'wb')
        file.write(res.content)
        file.close()
        print(name + '.pdf' + 'file saved')
    except:
        pass