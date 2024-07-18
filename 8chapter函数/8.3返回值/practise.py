# 练习 8.6：城市名 编写⼀个名为 city_country() 的函数，它接受
# 城市的名称及其所属的国家。这个函数应返回⼀个格式类似于下⾯的
# 字符串：
def city_country(city_name, country):
    ful_city = f"\"{city_name}, {country}\""
    return ful_city.title()


full_city = city_country('shanghai', 'china')
print(full_city)


# 练习 8.7：专辑 编写⼀个名为 make_album() 的函数，它创建⼀个
# 描述⾳乐专辑的字典。这个函数应接受歌⼿名和专辑名，并返回⼀个
# 包含这两项信息的字典。使⽤这个函数创建三个表⽰不同专辑的字
# 典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。
# 给 make_album() 函数添加⼀个默认值为 None 的可选形参，以便存
# 储专辑包含的歌曲数。如果调⽤这个函数时指定了歌曲数，就将这个
# 值添加到表⽰专辑的字典中。调⽤这个函数，并⾄少在⼀次调⽤中指
# 定专辑包含的歌曲数。
def make_album(singer_name, album_name, sing_num=None):
    album = {'singer': singer_name, 'albumName': album_name}
    if sing_num:
        album['sing_num'] = sing_num
    return album


albumInfo = make_album('zhou', 'mojiezuo', 12)
print(albumInfo)


# 练习 8.8：⽤户的专辑在为练习 8.7 编写的程序中，编写⼀个 while
# 循环，让⽤户输⼊歌⼿名和专辑名。获取这些信息后，使⽤它们来调
# ⽤ make_album() 函数并将创建的字典打印出来。在这个 while 循
# 环中，务必提供退出途径。

while True:
    print("我们现在要做一下关于歌手专辑信息的统计")
    singer = input("歌手的名字是啥")