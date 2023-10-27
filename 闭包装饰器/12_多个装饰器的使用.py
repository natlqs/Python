def check1(fn1):
    def inner1():
        print('登陆验证1')
        fn1()
    return inner1


def check2(fn2):
    def inner2():
        print('登陆验证2')
        fn2()
    return inner2


@check1     # @check1   ==>         comment() = check1(comment())
@check2     # @check2   ==>         comment() = check2(comment())
def comment():
    print('发表评论')


comment()
