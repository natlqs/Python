
def logging(fn):
    def inner(a, b):
        result = fn(a, b)
        return result

    return inner


@logging    # @logging ==>    sum_num(a, b) = logging(sum_num(a, b))
def sum_num(a, b):
    result = a + b
    # print(result)
    return result


result = sum_num(1, 2)
# sum_num(2, 3)
print(result)
