import requests
import re
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}

def db(page):
   # 1. 获取网页源代码
    num = (page - 1) * 25  # 页面参数规律是（页码－1）×25
    url = 'https://movie.douban.com/top250?start=' + str(num)
    res = requests.get(url, headers=headers).text
   # 2. 用正则表达式提取电影片名和图片网址
    p_title = '<img width="100" alt="(.*?)"'
    title = re.findall(p_title, res)
    p_img = '<img width="100" alt=".*?" src="(.*?)"'
    img = re.findall(p_img, res)
    p_score = '<span class="rating_num" property="v:average">(.*?)</span>'
    score = re.findall(p_score, res)
   # 3. 打印输出电影片名和图片网址，并下载图片
    for i in range(len(title)):
       print(str(i + 1) + '.' + title[i])
       print(score[i])
       print(img[i])
       res = requests.get(img[i])  # 开始下载图片
       file = open('.\\Python\\crawler\\requests & selenium\\images\\'+ str(num+i) + ' ' + score[i] + title[i] + '.jpg', 'wb')
       file.write(res.content)
       file.close()

for i in range(10):  # i是从0开始的序号，要加上1才是页码
   db(i + 1)
   print('第' + str(i + 1) + '页爬取成功！')