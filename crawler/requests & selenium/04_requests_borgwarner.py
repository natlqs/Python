import requests
url = 'https://www.baidu.com/s?tn=news&rtt=4&wd=博格華納&medium=0'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76'}
res = requests.get(url, headers = headers).text
print(res)