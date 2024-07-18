def build_profile(first, last, **user_info):
    """创建⼀个字典，其中包含我们知道的有关⽤户的⼀切"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')

print(user_profile)
