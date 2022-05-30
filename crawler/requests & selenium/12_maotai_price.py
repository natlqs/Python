from email import header
import requests

headers={'Referer':'https://finance.sina.com.cn/'}
urls =[ 'https://hq.sinajs.cn/list=sh600519', 'https://hq.sinajs.cn/list=sz002714']
for i in urls:
    res = requests.get(i, headers=headers).text
    res_split = res.split(',')  
    stock_name = res_split[0]
    open_price = res_split[1]       # 提取第2个元素（开盘价）
    pre_close_price = res_split[2]
    now_price = res_split[3]
    high_price = res_split[4]
    low_price = res_split[5]

    print('股票名称：' + stock_name)
    print('开盘价:' + open_price)
    print('昨日收盘价：' + pre_close_price)
    print('当前价格：' + now_price)
    print('最高价：' + high_price)
    print('最低价：' + low_price)