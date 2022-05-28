# -*- coding: utf-8 -*-
import requests
import re

url = 'http://www.baidu.com'
html = requests.get(url)
# html.encoding = 'utf-8'
if html.status_code == requests.codes.ok:
    pattern = input('please input pattern: ')
    result = re.findall(pattern, html.text)
    if result != None:
        print('%s occurs %d times' % (pattern, len(result)))
    else:
        print('Occurs 0 times' % pattern)
else:
    print('failed')
print(type(html))
print(html.text)