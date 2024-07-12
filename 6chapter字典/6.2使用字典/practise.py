# 练习 6.1：⼈ 使⽤⼀个字典来存储⼀个⼈的信息，包括名、姓、年龄
# 和居住的城市。该字典应包含键 first_name、last_name、age 和
# city。将存储在该字典中的每项信息都打印出来。
human = {
    'first_name':'shui',
    'last_name' : 'cc',
    'age' : '22',
    'city' : 'Maanshan',
}
print(human)

# 练习 6.2：喜欢的数 1 使⽤⼀个字典来存储⼀些⼈喜欢的数。请想出
# 5 个⼈的名字，并将这些名字⽤作字典中的键。再想出每个⼈喜欢的⼀
# 个数，并将这些数作为值存储在字典中。打印每个⼈的名字和喜欢的
# 数。为了让这个程序更有趣，通过询问朋友确保数据是真实的。
favorite_numbers = {
    'shui' : 20,
    'zhao' : 12,
    'zhou' : 66,
    'wang' : 37,
    "liu"  : 99,
}
print(favorite_numbers['liu'])
for key in favorite_numbers:
    print(key) 
for value in favorite_numbers.values():
    print(value)    
for key,value in favorite_numbers.items(): # 同时打印key和value的方法，网上搜的
    print(f"{key}喜欢的数字是{value}")
    
# 练习 6.3：词汇表 1 Python 字典可⽤于模拟现实⽣活中的字典。为避
# 免混淆，我们将后者称为词汇表。
words_list = {
    'for' : 'for循环',
    'range()' : '创建一个整数列表',
    'if' : 'if语句',
    'del' : '删除元素,删除之后元素会向左补齐',
    'remove()' : '删除指定的元素',
}
for key,value in words_list.items():
    print(f"{key}:{value}")