# 1 定义一个装饰器（装饰器的本质是闭包）
def check(fn):
    def inner():
        print('登录验证。。。')
        fn()

    return inner

# 需要被装饰的函数
def comment():
    print('发表评论')

#2 使用装饰器装饰函数（增加一个登录功能）
comment = check(comment)
comment()