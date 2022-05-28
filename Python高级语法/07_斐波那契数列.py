# 
def fb(num):
    a = 0
    b = 1
    # 记录生成了几个数字
    index = 0
    while index < num:
        result = a
        a, b = b, a + b
        yield result
        index += 1

f = fb(5)
# print(next(f))
print(next(f))
for i in f:
    print(i)