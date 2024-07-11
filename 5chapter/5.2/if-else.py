# if-elif-else 语句
age = 12 
if age < 4: 
    price = 0 
elif age < 18: 
    price = 25 
elif age < 65: 
    price = 40 
else:               # 用这个句子更直观 elif age >= 65: 
    price = 20 
print(f"Your admission cost is ${price}.") 

# 测试多个条件

# 假设玩家在游戏中消灭了⼀个外星⼈，请创
# 建⼀个名为 alien_color 的变量，并将其赋值为
# 'green'、'yellow' 或 'red'。

alien_color = 'yellow'
if alien_color == 'green':
    print('you get 5 points')
alien_color = 'green'
if alien_color == 'green':
    print('you get 5 points')
    
# 像练习 5.3 那样设置外星⼈的颜⾊，并编写
# ⼀个 if-else 结构。
if alien_color == 'green':
    print("you get 5 points")
else:
    print("you get 10 points")
# 执行else部分   
if alien_color == 'yellow':
    print("you get 5 points")
else:
    print("you get 10 points")

# 将练习 5.4 中的 if-else 结构改为 if-
# elif-else 结构。
if alien_color == 'green':
    score = 5
elif alien_color == 'yellow':
    score = 10
elif alien_color == 'red':
    score = 15
print(f"you get {score} points")
# 黄色的得分
alien_color = 'yellow'
if alien_color == 'green':
    score = 5
elif alien_color == 'yellow':
    score = 10
elif alien_color == 'red':
    score = 15
print(f"you get {score} points")
# 红色的得分
alien_color = 'red'
if alien_color == 'green':
    score = 5
elif alien_color == 'yellow':
    score = 10
elif alien_color == 'red':
    score = 15
print(f"you get {score} points")
# ⼈⽣的不同阶段 设置变量 age 的值，再编写⼀个 if-
# elif-else 结构，根据 age 的值判断这个⼈处于⼈⽣的哪个阶段。

age = 27
if age < 2:
    print("是个婴儿")
elif age >=2 and age < 4:
    print('是个幼儿')
elif age >=4 and age < 13:
    print('是个儿童')
elif age >=13 and age < 18:
    print('是个少年')   
elif age >=18 and age < 65:
    print('是个中青年')    
else:
    print("是个老年人")
    
# 喜欢的⽔果 创建⼀个列表，其中包含你喜欢的⽔果，再编
# 写⼀系列独⽴的 if 语句，检查列表中是否包含特定的⽔果。
favorite_fruits = ['apple','watermelon','orange']
fruit = 'apple'
if fruit in favorite_fruits:
    print(f"you really like {fruit}")
    