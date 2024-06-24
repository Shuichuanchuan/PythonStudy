name = ['zhou','wu','zhen','wang']
num = 0 
while num < len(name):
    print(f"{name[num].title()},hello how are you?")
    num = num + 1
# 数组的使用
name.append('zhao')
#append 追加 在数组末尾添加新元素

print(f"{name[-1].title()}\n")
#数组[-1]表示返回倒数第一个元素，-2倒数第二个以此类推

name.insert(0,'shui')
#insert()方法可以数组中间插入元素，
#不过数组内所有的元素都要从插入的位置向右移动一个位置
num = 0 
while num < len(name):
    print(name[num].title())
    num = num + 1
print("\n")

# 用del语句删除元素
del name[0]
print(name[0])
# 删除之后元素会向左补齐

#pop方法删除元素
print(name)
popped_name = name.pop()
print(name)
print(popped_name)
name.append("zhao")     #添加zhao为数组最后一个元素
# 也可以指定任意位置的元素删除，只需要在pop()里指定元素的位置
print(name)
first_name = name.pop(0)
print(name)
print(first_name)
name.insert(0,'zhou')   # 添加zhou为数组第一个元素

# 如果要从列表中删除⼀个元素，且不再以任何⽅式使⽤它，
# 就使⽤ del 语句；如果要在删除元素后继续使⽤它，就使⽤ pop() ⽅法。

