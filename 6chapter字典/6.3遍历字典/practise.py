# 练习 6.4：词汇表 2 现在你知道了如何遍历字典，请整理你为练习 6.3
# 编写的代码，将其中的⼀系列函数调⽤ print() 替换为⼀个遍历字典
# 中键和值的循环。确保该循环正确⽆误后，再在词汇表中添加 5 个
# Python 术语。当你再次运⾏这个程序时，这些新术语及其含义将⾃动
# 包含在输出中。
words_list = {
    'for' : 'for循环',
    'range()' : '创建一个整数列表',
    'if' : 'if语句',
    'del' : '删除元素,删除之后元素会向左补齐',
    'remove()' : '删除指定的元素',
    'sorted' : '给列表排序',
    'while' : 'while语句',
    
}

for key,value in words_list.items():
    print(f"{key} 表示{value}")
print("\n")
    
# 练习 6.5：河流 创建⼀个字典，在其中存储三条河流及其流经的国
# 家。例如，⼀个键值对可能是 'nile': 'egypt'。

rivers_dict = {
    '西湖' : '杭州',
    '银河' : '宇宙',
    '洞庭湖' : '湖北',
    '洱海' : '云南',
}

for key,value in rivers_dict.items():
    print(f"{key}在{value}")
print("\n")
for key in rivers_dict:
    print(key)
print("\n")
for value in rivers_dict.values():
    print(value)

# 练习 6.6：调查 在 6.3.1 节编写的程序 favorite_languages.py 中执⾏以
# 下操作。

inv_list = ['jen','sarah','edward','phil','john','li','manba']
favorite_languages = { 
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'rust', 
    'phil': 'python', 
    } 
for inv  in inv_list:
    if inv not in favorite_languages:
        print(f"Hello {inv} 希望您能来参加调查")
    else:
        print(f"{inv}，感谢您接受调查")