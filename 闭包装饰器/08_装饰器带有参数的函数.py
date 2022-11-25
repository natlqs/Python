def logging(fn):
    def inner(a, b):
        print(a, b)
        fn(a, b)

    return inner


@logging
# @logging ==>      sum_num(1, 2) = logging(sum_num(1, 2))
def sum_num(a, b):
    result = a + b
    print(result)


sum_num(1, 2)
