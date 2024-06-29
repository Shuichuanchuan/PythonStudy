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