# __call__方法
# 一个类里面一旦实现了__call__方法，那么这个类创建的对象就是一个可调用对象，可以像调用函数一样进行调用

class Check(object):
    def __call__(self, *args, **kwds): 
        print('我是call方法')

c = Check()
c()