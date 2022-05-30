# 1 定义一个装饰器（装饰器的本质是闭包）
def check(fn):
    def inner():
        print('登录验证。。。')
        fn()

    return inner


#2 使用装饰器装饰函数（增加一个登录功能）
# 解释器遇到@check 会立即执行 comment = check(comment)
@check
# 需要被装饰的函数
def comment():
    print('发表评论')

comment()