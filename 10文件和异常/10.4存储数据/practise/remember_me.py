from pathlib import Path
import json


def get_stored_username(path):
    """如果存储了⽤户名，就获取它"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username['username']
    else:
        return None


def get_new_username(path):
    """获取用户名以判断是否相符"""
    username = input("What is your name?: ")
    return username


def get_new_user_info(path):
    """提⽰⽤户输⼊用户信息"""
    user_info = {}
    username = input("What is your name?: ")
    user_info['username'] = username
    age = input("How old are you?: ")
    user_info['age'] = age
    fav_food = input("What food you like?: ")
    user_info['favorite food'] = fav_food

    contents = json.dumps(user_info)
    path.write_text(contents)
    return username


def greet_user():
    """问候⽤户，并指出其名字"""
    path = Path('username.json')
    new_name = get_new_username(path)
    username = get_stored_username(path)
    if new_name == username:
        print("it's right")
        if username:
            print(f"Welcome back, {username}!")
        else:
            username = get_new_user_info(path)
            print(f"We'll remember you when you come back, {username}!")
    else:
        print("username is wrong")
        greet_user()


def get_info():
    """获取用户信息"""
    path = Path('username.json')
    contents = path.read_text()
    infos = json.loads(contents)
    for key, value in infos.items():
        print(f"{key}:{value}")
    return infos


def judgment_user(path):
    """判断用户是谁"""
    path = Path('username.json')
    username = get_stored_username(path)


greet_user()
get_info()
