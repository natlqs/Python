def func01():
    print('func01 is show')

# # func01()      # 运行函数


# # 函数名存放函数所在空间的地址
print(func01)  # 打印函数的地址

# # 函数名也可以像普通变量一样赋值
func02 = func01
func02()
print(func02)


def foo(func):   # 将函数名当作参数传入函数内部
    func()
    print(func)


foo(func01)
