# 6.4.3 在字典中存储字典
users = {                       # 定义⼀个名为 users 的字典
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\t Full name: {full_name.title()}")
    print(f"\t Location: {location}")
