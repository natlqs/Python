# 外部函数
def config_name(name):
    # 内部函数
    def say_info(info):
        print(name + ":", info)

    return say_info


tom = config_name("tom")
tom("nihao")
tom("你在吗")

jerry = config_name("jerry")
jerry('nihao')
jerry('wozai')
