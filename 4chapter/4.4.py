# 切片 打印list给定范围的元素
players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print(players[0:3])
print(players[1:4])
print(players[:4])  # 没有指定起始索引的话，从头开始打印，反则同理。

print(players[-3:]) # 返回打印最后三个人
# 遍历切片
print("这里有三名我的队员")
for player in players[:3]:
    print(player.title())
print("\n")

# 复制列表
my_foods = ['rice','chips','ice cream']
friend_foods = my_foods[:]
print(f"My favorite foods are:{my_foods}")
print(f"\nMy friend's favorite foods are:{friend_foods}")
my_foods.append('cannoli')
friend_foods.append('nuddle')

# 演示一下在不使用切片的情况下复制列表
my_foods = ['rice','chips','ice cream']
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('nuddle')
print("我最爱的食物是：")
print(my_foods)
print("\n我friend最爱的食物是：")
print(friend_foods)
# 运行这段代码可以得出朋友和我喜爱的食物是一样的
# append()添加的cannoli 和 nuddle同时存在于两个列表中
# 实际上是因为friend_foods = my_foods 将两个列表相关联了
# 并没有将my的值赋予friend--指向同一个列表


# 选择你在本章编写的⼀个程序，在末尾添加⼏⾏代
# 码，以完成如下任务。
# 打印消息“The first three items in the list are:”，再使⽤切⽚来打印列
# 表的前三个元素。
my_foods = ['rice','chips','ice cream','cannoli','nuddle']
print(f"The first three items in the list are:{my_foods[0:3]}")
print(f"Three items from the middle of the list are:{my_foods[1:4]}")
print(f"The last three items in the list are:{my_foods[-3:]}")

# 练习 4.11：你的⽐萨，我的⽐萨 在你为练习 4.1 编写的程序中，创建
# ⽐萨列表的副本，并将其赋给变量 friend_pizzas，再完成如下任
# 务。
my_fruits = ['apple','orange','watermelon','cherry']
friend_fruits = my_fruits[:]
my_fruits.append('grape')
friend_fruits.append('pineapple')
print("My favorite fruits are:")
for fruits in my_fruits:
    print(fruits)   
print("My friend favorite fruits are:")
for fruits in friend_fruits:
    print(fruits)