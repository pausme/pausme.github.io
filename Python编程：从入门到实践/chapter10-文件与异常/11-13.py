import json
filename = "favorite_number.json"

def read_favorite_number():
    try:
        with open(filename) as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        print(f"I konw your favorite number! It's {favorite_number}.")

def get_favorite_number():
    with open(filename,"w") as f:
        favorite_number = input("输入你最喜欢的数：")
        json.dump(favorite_number,f)

get_favorite_number()
read_favorite_number()


def favorite_number():
    try:
        with open(filename) as f:
            favorite_number = json.load(f)
    except:
        with open(filename,"w") as f:
            favorite_number = input("输入自己最喜欢的数：")
            json.dump(favorite_number,f)
    else:
        print(f"I know your favorite number! It's {favorite_number}.")

favorite_number()
favorite_number()

def get_stored_username():
    filename = "username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What is your name?")
    filename = "username.json"
    with open(filename,"w") as f:
        json.dump(username,f)
    return username

def greet_user():
    username =  get_stored_username()
    if username:
        print(username)
        flag = input("用户名是否正确？输入(y/n)")
        if flag.upper() == "Y":
            print(f"Welcome back, {username}")
        elif flag.upper() == "N":
            get_new_username()
        else:
            flag = input("请输入y/n！！！")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}")

greet_user()
