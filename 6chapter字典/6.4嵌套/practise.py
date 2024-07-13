# 练习 6.7：⼈们 在为练习 6.1 编写的程序中，再创建两个表⽰⼈的字
# 典，然后将这三个字典都存储在⼀个名为 people 的列表中。遍历这
# 个列表，将其中每个⼈的所有信息都打印出来。
human = {
    'shuicc': {
        'first_name': 'shui',
        'last_name': 'cc',
        'age': '22',
        'city': 'beijing',
    },
    'zhou': {
        'first_name': 'zhou',
        'last_name': 'x',
        'age': '21',
        'city': 'your city',
    },
    'gang': {
        'first_name': 'li',
        'last_name': 'm',
        'age': '45',
        'city': 'my city',
    }
}

for info in human.values():
    full_name = f"{info['first_name'].title()}{info['last_name']}"
    print(f"姓名是：{full_name}")
    print(f"年龄是：{info['age']}")
    print(f"居住在：{info['city'].title()}\n")

# 练习 6.8：宠物创建多个表⽰宠物的字典，每个字典都包含宠物的类
# 型及其主⼈的名字。将这些字典存储在⼀个名为 pets 的列表中，再
# 遍历该列表，并将有关每个宠物的所有信息打印出来。
pets = {
    '黄土狗': {
        'type': '土狗',
        'master': '李强',
    },
    '黑土狗': {
        'type': '土狗',
        'master': '王强',
    },
    '绿土狗': {
        'type': '土狗',
        'master': '张强',
    },
}
for name, info in pets.items():
    print(f"{name}是{info['type']},他的主人是：{info['master']}")
print("\n")
# 练习 6.9：喜欢的地⽅ 创建⼀个名为 favorite_places 的字典。
# 在这个字典中，将三个⼈的名字⽤作键，并存储每个⼈喜欢的 1〜3 个
# 地⽅。为让这个练习更有趣些，让⼀些朋友说出他们喜欢的⼏个地
# ⽅。遍历这个字典，并将其中每个⼈的名字及其喜欢的地⽅打印出来。

favorite_places = {
    'shui': ['shanxi', 'guangzhou', 'wdc'],
    'zhou': ['xinjiang', 'shanghai', 'xizang'],
    'li': ['beijing']
}
for name, places in favorite_places.items():
    if len(places) == 1:
        for place in places:
            print(f"{name}最喜欢的地方是：{place}")

    else:
        print(f"{name}喜欢的地方有：")
        for place in places:
            print(f"\t{place.title()}")

# 练习 6.10：喜欢的数 2 修改为练习 6.2 编写的程序，让每个⼈都可以
# 有多个喜欢的数字，然后将每个⼈的名字及其喜欢的数打印出来。
cities = {
    'beijing': {
        'country': '中国',
        'population': '1000w',
        'fact': '中国的首都',
    },
    'shanghai': {
        'country': '中国',
        'population': '2000w',
        'fact': '宇宙的首都',
    },
    'guangzhou': {
        'country': '中国',
        'population': '9000w',
        'fact': 'Wakanda',
    }
}
for city, infos in cities.items():
    print(f"{city.title()}:")
    for info in infos:
        print(f"\t{info}:{infos[info]}")

