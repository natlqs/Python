from PIL import Image
import numpy as np
from collections import Counter
from wordcloud import WordCloud, ImageColorGenerator
from imageio import imread
import jieba

# 1. 读取文本内容并用jieba库的cut()函数进行分词
report =open('.\\Python\\crawler\\requests & selenium\\信托行业年度报告.txt', 'r', encoding='utf-8').read()
words = jieba.cut(report)
report_words = []

# 2.通过for循环提取长度大于等于4个字的词
for word in words:
    # print(word)
    if len(word) >= 4:  
        report_words.append(word)  # 将长度大于等于4个字的词放入列表
# print(report_words)
result = Counter(report_words).most_common(50) # 取最多的50组
# print(result)
content = ' '.join(report_words) # 把列表转换为字符串

# 3.按特定形状和特定颜色绘制云图
# (1) 获取词云图的形状蒙版
background_pic = '.\\Python\\crawler\\requests & selenium\\weibo.jpg'
images = Image.open(background_pic) # 打开形状蒙版图片
maskImages = np.array(images)   # 将形状蒙版图片转换为数值数组
# print(maskImages)
#(2) 按照形状蒙版绘制词云图
wc = WordCloud(font_path='simhei.ttf', #字体文件路径
                background_color='white',
                width=1000,
                height=600,
                mask=maskImages).generate(content)

# (3) 修改词云图的颜色
back_color = imread(background_pic)
image_colors = ImageColorGenerator(back_color)
wc.recolor(color_func=image_colors)
wc.to_file('.\\Python\\crawler\\requests & selenium\\词云图+自定义形状.png')    # 导出成PNG格式图片