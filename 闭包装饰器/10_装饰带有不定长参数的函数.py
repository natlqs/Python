
def logging(fn):
    def inner(*args, **kwargs):
        fn(*args, **kwargs)

    return inner
@logging
def sum_num(*args,**kwargs):
    print(args, kwargs)

sum_num(1, 2, 3, age='18')