# 返回简单的值
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回标准格式的姓名"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('jimi', 'hooker', 'lee')
print(musician)
# 让实参变成可选的
# 假设要扩展 get_formatted_name() 函数，使其除了名和姓之外还可以处理中间名
# 并⾮所有⼈都有中间名。如果调⽤这个函数时只提供了名和姓，它将不能正确地运⾏
# 让中间名变成可选的，可给形参 middle_name 指
# 定默认值（空字符串），在⽤户不提供中间名时不使⽤这个形参
