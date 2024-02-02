#订单信息管理视图文件
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from datetime import datetime

from myadmin.models import Orders,OrderDetail,Payment

def index(request,pIndex=1):
    ''' 浏览订单信息 '''
    pass

def insert(request):
    ''' 执行订单添加 '''
    try:
        #执行订单信息的添加
        od = Orders()
        od.shop_id = request.session['shopinfo']['id']
        od.member_id = 0
        od.user_id = request.session['webuser']['id']
        od.money = request.session['total_money']
        od.status = 1 #订单状态:1过行中/2无效/3已完成
        od.payment_status = 2 #支付状态:1未支付/2已支付/3已退款
        od.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        od.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        od.save()

        #执行支付信息添加
        op = Payment()
        op.order_id = od.id #订单id号
        op.member_id = 0
        op.type = 2
        op.bank = request.GET.get("bank",3) #收款银行渠道:1微信/2余额/3现金/4支付宝
        op.money = request.session['total_money']
        op.status = 2 #支付状态:1未支付/2已支付/3已退款
        op.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        op.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        op.save()

        #执行订单详情的添加
        cartlist = request.session.get("cartlist",{}) #获取购物车中的菜品信息
        #遍历购物车中的菜品并添加到订单详情中
        for item in cartlist.values():
            ov = OrderDetail()
            ov.order_id = od.id  #订单id
            ov.product_id = item['id']  #菜品id
            ov.product_name = item['name'] #菜品名称
            ov.price = item['price']     #单价
            ov.quantity = item['num']  #数量
            ov.status = 1 #状态:1正常/9删除
            ov.save()

        del request.session["cartlist"]
        del request.session['total_money']
        return HttpResponse("Y")
    except Exception as err:
        print(err)
        return HttpResponse("N")

def detail(request):
    ''' 加载订单详情 '''
    pass

def status(request):
    ''' 修改订单状态 '''
    pass