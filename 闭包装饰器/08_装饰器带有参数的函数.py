def logging(fn):
    def inner(a, b):
        fn(a, b)

    return inner
@logging
def sum_num(a,b):
    result = a + b
    print(result)

sum_num(1, 2)