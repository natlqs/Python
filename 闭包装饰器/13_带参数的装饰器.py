def logging(flag):
    def decorator(fn):
        def inner(num1, num2):
            if flag == '+':
                print('正在努力加法计算...')
            elif flag == '-':
                print('正在努力减法计算...')
            result = fn(num1, num2)
            return result
        return inner
    return decorator


# 被带有参数的装饰器装饰的函数
@logging('+')
# @logging('-')
def add(a, b):
    result = a + b
    return result


# 执行函数
result1 = add(1, 3)
print(result1)
