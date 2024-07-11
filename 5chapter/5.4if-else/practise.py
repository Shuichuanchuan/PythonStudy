# 练习 5.8：以特殊⽅式跟管理员打招呼 创建⼀个⾄少包含 5 个⽤户名
# 的列表，并且其中⼀个⽤户名为 'admin'。想象你要编写代码，在每
# 个⽤户登录⽹站后都打印⼀条问候消息。遍历⽤户名列表，向每个⽤
# 户打印⼀条问候消息。

user_ids = ['admin','shui','botter','zzz','happy']
for user_id in user_ids:
    if user_id == 'admin':
        print(f"Hello {user_id},wourld you like to see a status report?")
    else:
        print(f"Hello {user_id},thank you for logging in again.")
        
# 练习 5.9：处理没有⽤户的情形 在为练习 5.8 编写的程序中，添加⼀
# 条 if 语句，检查⽤户名列表是否为空。
print('\n')
user_ids = []
if user_ids:
    for user_id in user_ids:
        if user_id == 'admin':
            print(f"Hello {user_id},wourld you like to see a status report?")
        else:
            print(f"Hello {user_id},thank you for logging in again.")
else:
    print('We need to find some users!')
print('\n')
# 练习 5.10：检查⽤户名 按照下⾯的说明编写⼀个程序，模拟⽹站如
# 何确保每个⽤户的⽤户名都独⼀⽆⼆。
current_users = ['admin','shui','botter','zzz','happy'] # 创建用户名列表
current_users_1 =[current_user.lower() for 
                  current_user in current_users ]   # 创建用户名小写列表
new_users = {'yaya','huhu','shui','zzz','botter'}   # 创建新加用户名列表
for new_user in new_users:
    if new_user.lower() in current_users_1:         # 比较小写列表
         print(f"{new_user}已被占用，请再输入一个您喜欢的用户名")
    else:
        print(f"恭喜，{new_user}未被占用，您可以使用这个用户名")
print('\n')
# 练习 5.11：序数 序数表⽰顺序位置，如 1st 和 2nd。序数⼤多以 th 结
# 尾，只有 1st、2nd、3rd 例外。
numbers = [number for number in range(1,10)]    # 创建1~9的数字列表
for number in numbers:                          # 遍历列表
    print(number)
for number in numbers:                          # 打印序数
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    else:
        print(f'{number}th')
    