# 闭包的构成条件
# 在函数嵌套（函数里面定义函数）的前提下
def func_out(num1):
    def func_inner(num2):
    # 内部函数使用了外部函数的变量（还包括外部函数的参数）
        # print(num1, num2)
        num = num1 + num2
        print('现在的值：', num)
    # 外部函数返回了内部函数， 返回的是函数的地址
    return func_inner

# 创建闭包实例
f = func_out(10)
# print(f)
# 执行闭包， 相当于执行内部函数
f(1)
f(2)
f(10)