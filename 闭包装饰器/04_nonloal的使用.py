# 外部函数
def func_out(num1):
    # 内部函数
    def func_inner(num2):
        # 可以修改闭包内使用的外部函数变量使用nonlocal关键字来完成
        nonlocal num1
        num1 = num2 + 10

    print(num1)
    func_inner(10)
    print(num1)
    return func_inner

# num1 = 10
# f = func_out(10)
# 调用闭包= 内部函数 num2 = 10
# f(10)


func_out(10)
