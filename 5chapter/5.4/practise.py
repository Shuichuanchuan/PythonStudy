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