account = {
    "is_authenticated": False,       # if login change this to True
    "username": "alex",             # user information in DB
    "password": "abc123"            # password in DB
}


def login(func):
    def inner():
        if account["is_authenticated"] is False:
            username = input('user:')
            password = input("password:")
            if username == account["username"] and password == account["password"]:
                print("welcome login...")
                account["is_authenticated"] = True
            else:
                print("wrong username or password!")
        if account["is_authenticated"] is True:
            func()
    return inner        # 注意这里只返回inner的内存地址，不执行


def home():
    print("---home---")


@login
def america():
    print("---america---")


@login
def japan():
    print("---japan---")


def henan():
    print("---henan---")


home()
# america = login(america)    # 这次执行login返回的是inner的内存地址，inner at 0x101762840
# print(america)

# japan = login(japan)

# print(japan)
america()
japan()
