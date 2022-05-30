class Check(object):
    def __init__(self, fn):
        self.__fn = fn
    def __call__(self, *arg, **kwargs):
        print('登录')
        self.__fn()

@Check              # comment = Check(comment)
def comment():
    print('发表评论')

comment()