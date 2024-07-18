# 练习 8.12：三明治 编写⼀个函数，它接受顾客要在三明治中添加的
# ⼀系列⾷材。这个函数只有⼀个形参（它收集函数调⽤中提供的所有
# ⾷材），并打印⼀条消息，对顾客点的三明治进⾏概述。调⽤这个函
# 数三次，每次都提供不同数量的实参。
def make_pizza(*toppings):
    print("配料有：")
    for topping in toppings:
        print(topping)


make_pizza('牛肉', '臭豆腐', '辣椒')


# 练习 8.13：⽤户简介 复制前⾯的程序 user_profile.py，在其中调⽤
# build_profile() 来创建有关你的简介。在调⽤这个函数时，指定
# 你的名和姓，以及三个⽤来描述你的键值对。
def build_profile(first, last, **user_info):
    """创建⼀个字典，其中包含我们知道的有关⽤户的⼀切"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    for user in user_info.items():
        print(user)
    return user_info


user_profile = build_profile('水', '村川',
                             location='princeton',
                             field='physics')
print(user_profile)


# 练习 8.14：汽⻋ 编写⼀个函数，将⼀辆汽⻋的信息存储在字典中。
# 这个函数总是接受制造商和型号，还接受任意数量的关键字实参。在
# 调⽤这个函数时，提供必不可少的信息，以及两个名值对，如颜⾊和
# 选装配件。这个函数必须能够像下⾯这样调⽤：
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# 打印返回的字典，确认正确地处理了所有的信息。
def make_car(manufacturer, model, **car_info):
    car_info['制造商'] = manufacturer
    car_info['型号'] = model
    return car_info


car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)