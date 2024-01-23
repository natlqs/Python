from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from myapp.models import Users

# Create your views here.
def home(request):
    return HttpResponse("Hello, World! <br/> <a href='/users'>用户信息管理</a>")
def add(request):
    return HttpResponse("adding...")
def find(request, id=0,name=''):
    return HttpResponse(f"finding...{id} results, and name is {name}")
def update(request):
    return HttpResponse("updating...")
def delete(request):
    return HttpResponse("deleting...")
def edit(request):
    return HttpResponse("editing...")
def jump(request):
    print(reverse("add"))   # reverse()函数可以通过路由名称反向解析出URL，这里返回URL的名称，
    # 然后通过这个名称可以跳转到相应的URL
    print(reverse("index"))
    # return HttpResponse("jumping...")
    return redirect("add")   # redirect()函数可以直接跳转到相应的URL

# 正则表达式匹配
def fun(request, year, month):
    return HttpResponse(f"this is a regular pattern..., date is {year}, month is {month}")

# 自定义错误页面
def error_404(request, exception):
    return render(request, '404.html', status=404)


# 数据库操作 测试
def databases(request):
    # # 增加数据操作
    # user = Users()    # 实例化一个新对象(空对象)
    # user.name = "Tom"
    # user.age = 25
    # user.phone = "13800138000"
    # user.save()   # 新对象就是添加，已存在则是修改


    # # 删除数据操作
    # user = Users.objects    # 获取Users的model对象
    # user6 = user.get(id=6)  # 获取id为6的用户对象
    # user6.delete()   # 删除用户对象


    # # 更新数据操作
    # user = Users.objects
    # user1 = user.get(id=1)
    # user1.name = "Jerry"
    # user1.age = 26
    # user1.phone = "13800138001"
    # user1.save()


    # # 查询数据操作
    user = Users.objects  # 获取Users的model操作对象
    users = user.all()   # 获取所有用户对象

    ulist = users.filter(age__gt=25)   # 过滤出所有年龄大于25的用户对象, gt =》greater than 大于
    print("过滤出所有年龄大于25的用户对象")
    for u in ulist:
        print(u.name, u.age, u.phone)   # 打印用户信息)
    ulist = users.filter(age__gte=25)   # 过滤出所有年龄大于等于25的用户对象, gte =》greater than or equal 大于等于
    print("过滤出所有年龄大于等于25的用户对象")
    for u in ulist:
        print(u.name, u.age, u.phone)   # 打印用户信息)
    ulist = users.filter(age__lt=25)   # 过滤出所有年龄小于25的用户对象, lt =》less than 小于
    print("过滤出所有年龄小于25的用户对象")
    for u in ulist:
        print(u.name, u.age, u.phone)   # 打印用户信息)ulist = users.filter(age__lte=25)   # 过滤出所有年龄小于等于25的用户对象, lte =》less than or equal 小于等于
    ulist = users.filter(age__exact=25)   # 过滤出所有年龄等于25的用户对象, exact =》exactly 精确匹配
    print("过滤出所有年龄等于25的用户对象")
    for u in ulist:
        print(u.name, u.age, u.phone)   # 打印用户信息)ulist = users.filter(name__exact='Tom')   # 过滤出所有名称为'Tom'的用户对象
    ulist = users.filter(name__contains='o')   # 过滤出所有包含'o'的用户对象
    for u in ulist:
        print(u.name, u.age, u.phone)   # 打印用户信息)ulist = users.filter(name__startswith='T')   # 过滤出所有以'T'开头的用户对象
    ulist = users.filter(name__endswith='y')   # 过滤出所有以'y'结尾的用户对象
    for u in ulist:
        print(u.name, u.age, u.phone)   # 打印用户信息)ulist = users.filter(name__icontains='t')   # 过滤出所有包含'T'或't'的用户对象
    ulist = users.filter(name__iexact='Tom')   # 过滤出所有名称为'Tom'的用户对象
    ulist = users.filter(name__in=['Tom', 'Jerry'])   # 过滤出所有名称为'Tom'或'Jerry'的用户对象
    ulist = users.filter(age__range=(20, 30))   # 过滤出所有年龄在20到30之间的用户对象
    ulist = users.filter(age__lt=25, age__gt=20)   # 过滤出所有年龄在20到24之间的用户对象
    ulist = users.filter(age__isnull=True)   # 过滤出所有年龄为空的用户对象
    ulist = users.filter(phone__regex=r'1380013800\d')   # 过滤出所有电话号码以'1380013800'开头的用户对象
    ulist = users.filter(name__iregex=r'T\w+')   # 过滤出所有名称包含以'T'开头的单词的用户对象
    ulist = users.order_by('age')   # 按照年龄排序
    ulist = users.order_by('-age')   # 按照年龄倒序排序
    ulist = users.order_by('name')   # 按照名称排序
    ulist = users.order_by('-name')   # 按照名称倒序排序
    ulist = users.values('name', 'age')   # 按照名称和年龄显示用户信息
    ulist = users.values_list('name', 'age')   # 按照名称和年龄显示用户信息
    ulist = users.distinct()   # 按照名称和年龄显示用户信息
    ulist = users.count()   # 统计用户数量
    for u in users:
        print(u.name, u.age, u.phone)   # 打印用户信息

    return HttpResponse("databases...")

# 浏览用户信息
def indexUsers(request):
    try:
        ulist = Users.objects.all()
        context = {"userslist":ulist}
        return render(request, 'myapp/users/index.html',context)    # 加载模板
    except:
        return HttpResponse("没有找到用户信息！")


# 加载添加用户信息表单
def addUsers(request):
    return render(request, "myapp/users/add.html")

# 执行用户信息添加
def insertUsers(request):
    try:
        ob = Users()
        # 从表单中获取要添加的信息，并封装到ob对象中
        ob.name = request.POST['name']
        ob.age = request.POST['age']
        ob.phone = request.POST['phone']
        ob.save()   # 执行保存
        context={"info": "添加成功!"}
    except:
        context={"info": "添加失败!"}

    return render(request, "myapp/users/info.html", context)

    

# 执行用户信息删除
def delUsers(request, uid=0 ):
    try:
        ob = Users.objects.get(id=uid)        # 获取要删除的数据
        ob.delete()     # 执行删除操作
        context={"info": "删除成功!"}
    except:
        context={"info": "删除失败!"}

    return render(request, "myapp/users/info.html", context)

 
    pass

# 加载用户信息修改表单
def editUsers(request, uid=0):
    try:
        ob=Users.objects.get(id=uid)    #获取要修改的数据
        context = {'user':ob}
        return render(request, 'myapp/users/edit.html', context)
    except:
        context = {"info": "没有找到要修改的数据"}
        return render(request, "myapp/users/info.html", context)

# 执行用户信息修改
def updateUsers(request):
    try:
        uid= request.POST['id']     # 获取要修改数据的id号
        ob = Users.objects.get(id=uid)  # 查询要修改的数据
        # 从表单中获取要添加的信息，并封装到ob对象中
        ob.name = request.POST['name']
        ob.age = request.POST['age']
        ob.phone = request.POST['phone']
        ob.save()   # 执行保存
        context={"info": "修改成功!"}
    except:
        context={"info": "修改失败!"}

    return render(request, "myapp/users/info.html", context)