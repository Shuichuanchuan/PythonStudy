# sort()方法对list永久排序
cars = ['bmw','audi','toyota','sbaru']
print(cars)
cars.sort(reverse=False)    # true表示反序
print(cars)

# sorted()函数可以进行临时排序
cars = ['bmw','audi','toyota','sbaru']
print("here is original list:")
print(cars)

print("\nhere is the sorted list:")
print(sorted(cars,reverse=True))       # sorted 也可以向reverse传递参数True/false

print("\nhere is original list again:")
print(cars)

# reverse() 可以永久反转数组的元素 当然只要在调用一次就可以反转成原来的list
cars.reverse()
print(cars)

# len()函数可以获取列表的长度
print(len(cars))

# 列出五个你想去旅游的地方
location = ['new yerk','bei jing','north','shang hai','xi an']
print(f"初始：\n{location}")
print(f"{sorted(location)}")# 用sorted改变顺序打印，但不改变原本的元素排序
print(location)
print(sorted(location,reverse=True))# sorted反向排序字母开头
print(location)
location.reverse()
print(location)
location.reverse()
print(location)
#sort()
location.sort(reverse=False)
print(f"sort:\n{location}")
location.sort(reverse=True)
print(f"sort:\n{location}")

guest_list = ['zy','fq','lal','yyj','zx']
print(f"嘉宾一共有：{len(guest_list)}个人")
