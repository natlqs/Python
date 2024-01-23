from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from PIL import Image, ImageDraw, ImageFont
import random

# Create your views here.
def index(request):
    return render(request, "myapp/index.html")

def resp01(request):
    # 模板返回数据
    return HttpResponse("<h3>一种简单的视图</h3>")

def resp02(request):
    # 直接返回一个404，没有去加载404的模板页面
    return HttpResponseNotFound("<h3>ResponseNotFoud</h3>")
    # 可以直接返回一个status状态码
    # return HttpResponse(status=403)
    # 返回一个404的错误页面
    # raise Http404("Poll does not exist")

# 重定向
def resp03(request):
    # redirect重定向，reverse反向解析url地址
    # return redirect(reverse('response02'))

    # 执行一段js代码，用js进行重定向
    return HttpResponse('<script>alert("添加成功");location.href="/resp02";</script>')

    # 加载一个提醒信息的跳转页面
    # context = {'info':'数据添加成功', 'u':'response02'}
    # return render(request, 'info.html', context)
    # return HttpResponseNotFound("<h3>ResponseNotFoud</h3>")

# 基于类的视图方法
class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello View!")

# json 数据响应，将数据转成json格式响应
def resp05(request):
    data = [
        {'id':1001, 'name':'zhangsan', 'age':20},
        {'id':1002, 'name':'xiaohong', 'age':23},
        {'id':1003, 'name':'wanger', 'age':24},
        {'id':1004, 'name':'lisi', 'age':22},
    ]
    return JsonResponse({'data':data})  # 必须以字典的方式响应

# Cookie的使用
def resp06(request):
    # # 获取当前的响应对象
    # response = HttpResponse("Cookie的设置")

    # print(request.COOKIES.get('a', None))
    # # 使用响应对象进行Cookie的设置
    # response.set_cookie('a', 'abc')

    # # 返回响应对象
    # return response


    ## 利用cookie实现一个计数器
    # 读取
    m = request.COOKIES.get('num', None)
    if m:
        m=int(m)+1
    else:
        m=1
    # 获取当前的响应对象
    response = HttpResponse("Cookie记录的计数器值：" + str(m))
    # 使用响应对象进行cookie的设置
    response.set_cookie('num', m)
    # 返回响应对象
    return response
    
# 测试request对象
def resp07(request):

    print("请求路径", request.path)
    print("请求方法", request.method)
    print("请求编码", request.encoding)
    # print(request.GET)
    print(request.GET['id'])
    print(request.GET.get('name'))
    print(request.GET.get('age', 0))


    return HttpResponse("测试request请求对象")

# 验证码的输出
def verifycode(request):
    # 引入绘图模块
    # from PIL import Image, ImageDraw, ImageFont
    # 引入随机函数模块
    # import random
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width=100
    height=25
    # 创建画面对象
    im=Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy= (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1= 'ABCD123EFGHIJK456LMNOPQRE789TUVWXYZ0'
    # 随机选4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象
    font = ImageFont.truetype('static/ariali.ttf', 23)
    # font = ImageFont.load_default().font
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session， 用于做进一步验证
    # request.session['verifycode']  = rand_str
    # 内存文件操作 --> 此方法为python3的
    import io
    buf = io.BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给哭护短，MTIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')
     