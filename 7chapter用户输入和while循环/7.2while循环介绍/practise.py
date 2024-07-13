# 练习 7.4：⽐萨配料 编写⼀个循环，提⽰⽤户输⼊⼀系列⽐萨配料，
# 并在⽤户输⼊ 'quit' 时结束循环。每当⽤户输⼊⼀种配料后，都打
# 印⼀条消息，指出要在⽐萨中添加这种配料。
prompt = "请添加您想要的配料：（输入quit以退出程序）"
active = True   # 定义一个flag
dish_list = []  # 创建一个空列表以便存储配料
while active:   # 判断flag是否为true
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        dish_list.append(message)
        print(f"添加{message}")
print("\n您总共加了这么多配料：")  # 打印配料表
for dish in dish_list:
    print(f"{dish}")

# 练习 7.5：电影票 有家电影院根据观众的年龄收取不同的票价：不到
# 3 岁的观众免费；3（含）〜12 岁的观众收费 10 美元；年满 12 岁的观
# 众收费 15 美元。请编写⼀个循环，在其中询问⽤户的年龄，并指出其票价。
prompt = "请问您年龄多大："
active = True       # 立一个flag
while active:
    age = input(prompt)
    if age == 'quit':   # 判断是否quit，是就break
        break
    age = int(age)
    if age < 3:
        print("三岁以下是免票的")
    elif 3 <= age <= 12:
        print("您得付10块钱")
    else:
        print("您得付15块钱")

