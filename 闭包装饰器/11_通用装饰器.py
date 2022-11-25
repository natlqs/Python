def logging(fn):
    def inner(*args, **kwargs):
        result = fn(*args, **kwargs)
        return result
    return inner


@logging        # @logging ==>      sum_num = logging(sum_num(*args, **kwargs))
def sum_num(*args, **kwargs):
    print(args, kwargs)


sum_num(1, 2, 3, age='18')
