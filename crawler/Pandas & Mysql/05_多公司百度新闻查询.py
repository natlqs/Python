from unittest import result
import requests
import re
import pandas as pd


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50'}

def baidu(company):
    url = 'https://www.baidu.com/s?rtt=4&tn=news&word=' + company
    res = requests.get(url, headers=headers).text
    p_titie = '<a href=".*?" target="_blank" class="news-title-font_1xS-F" aria-label="标题：(.*?)" data-click="'
    p_href = '<h3 class="news-title_1YtI1 "><a href="(.*?)" target="_blank" class="news-title-font_1xS-F'
    title = re.findall(p_titie, res)
    href = re.findall(p_href, res)
    # print(title)
    # print(href)
    company_list = []
    for i in range(len(title)):
        company_list.append(company)    # 添加公司名称
        # title[i] = re.sub('<.*?>', '', title[i])
        
    df = pd.DataFrame()
    df['公司'] = company_list
    df['标题'] = title
    df['网址'] = href
    return df

df_all = pd.DataFrame() # 创建一个空DataFrame，用于汇总数据表格
companies = ['华能信托', '阿里巴巴', '万科集团']
for i in companies:
    result = baidu(i)
    df_all = df_all.append(result)
    print(i + '百度新闻爬取成功')
        
df_all.to_excel('.\\Python\\crawler\\Pandas & Mysql\\百度新闻-多家.xlsx', index=False)      # index = False 表示忽略行索引