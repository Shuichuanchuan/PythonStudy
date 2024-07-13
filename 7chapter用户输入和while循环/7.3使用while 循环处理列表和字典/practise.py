# 练习 7.8：熟⾷店 创建⼀个名为 sandwich_orders 的列表，其中
# 包含各种三明治的名字，再创建⼀个名为 finished_sandwiches
# 的空列表。遍历列表 sandwich_orders，对于其中的每种三明治，
# 都打印⼀条消息，如“I made your tuna sandwich.”，并将其移到列表
# finished_sandwiches 中。当所有三明治都制作好后，打印⼀条消
# 息，将这些三明治列出来。

# sandwich_orders = ['臭豆腐三明治', '皮蛋三明治', '无花果三明治']
# finished_sandwiches = []
# while len(sandwich_orders) > 0:     # 判断列表是否为空
#     print(f"I made your {sandwich_orders[0]}")
#     finished_sandwiches.append(sandwich_orders[0])      # 制作完的三明治添加到finish
#     sandwich_orders.remove(sandwich_orders[0])
#
# for finished_sandwich in finished_sandwiches:
#     print(f"This is your {finished_sandwich}")

# 练习 7.9：五⾹烟熏⽜⾁卖完了 使⽤为练习 7.8 创建的列表
# sandwich_orders，并确保 'pastrami' 在其中⾄少出现了三次。
# 在程序开头附近添加这样的代码：先打印⼀条消息，指出熟⾷店的五
# ⾹烟熏⽜⾁（pastrami）卖完了；再使⽤⼀个 while 循环将列表
# sandwich_orders 中的 'pastrami' 都删除。确认最终的列表
# finished_sandwiches 中未包含 'pastrami'。
sandwich_orders = ['臭豆腐三明治', '五香烟熏牛肉', '皮蛋三明治',
                   '五香烟熏牛肉', '无花果三明治', '五香烟熏牛肉']
finished_sandwiches = []
print("不好意思，五香烟熏牛肉卖完了")

while len(sandwich_orders) > 0:     # 判断列表是否为空
    while '五香烟熏牛肉' in sandwich_orders:
        sandwich_orders.remove('五香烟熏牛肉')
    print(f"I made your {sandwich_orders[0]}")
    finished_sandwiches.append(sandwich_orders[0])      # 制作完的三明治添加到finish
    sandwich_orders.remove(sandwich_orders[0])

for finished_sandwich in finished_sandwiches:
    print(f"This is your {finished_sandwich}")

# 练习 7.10：梦想中的度假胜地 编写⼀个程序，调查⽤户梦想中的度
# 假胜地。使⽤类似于“If you could visit one place in the world, where
# would you go?”的提⽰，并编写⼀个打印调查结果的代码块。
dream_places = []
name_lists = []
dream_active = True
while dream_active:
    name = input("请问您的姓名是：")
    place = input("如果让你选择一个地方，你梦想中的度假胜地是哪里：")
    dream_places.append(place)
    name_lists.append(name)
    repeat = input(f"{name}你想让别人回答这个问题吗？（是/否）")
    if repeat == '否':
        dream_active = False


for name, place in zip(name_lists, dream_places):   # zip()可以遍历对应关系的列表
    print(f"{name}想去的地方是{place}")

