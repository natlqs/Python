
def logging(fn):
    def inner(a, b):
        result = fn(a, b)
        return result

    return inner
@logging
def sum_num(a,b):
    result = a + b
    return result
result = sum_num(1, 2)
print(result)