# range() 函数
for value in range(1, 5):
    print(value)
    # 注意函数只会打印1,2,3,4没有5，常见的差一行为
    # 不指定起始数的时候，默认0开始

# range()创建数值列表
numbers = list(range(1, 6))
print(numbers)
# range()第三个参数是步长
even_numbers = list(range(2, 11, 2))
print(f"步长为2：{even_numbers}")

# range()创建乘方列表
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

# max min sum 简单的统计计算
digits = []
for number in range(10):
    digit = number
    digits.append(number)
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))

#列表推导式✨
squares = [value**2 for value in range(1,11)]
print(squares)

# 使⽤⼀个 for 循环打印数 1〜20（含）
for number1 in range(1,21):
    print(number1)
print("\n")
# 创建⼀个包含数 1〜1 000 000 的列表，再使⽤⼀个
# for 循环将这些数打印出来。（如果输出的时间太⻓，按 Ctrl + C 停⽌
# 输出，或关闭输出窗⼝。）
# 创建列表
# list_num = []
# for num in range(1,1000001):
#     list_num.append(num)
# # 打印列表
# for num in list_num:
#     print(num)

# 创建⼀个包含数 1〜1 000 000 的列表，再使⽤
# min() 和 max() 核实该列表确实是从 1 开始、到 1 000 000 结束的。
# 另外，对这个列表调⽤函数 sum()，看看 Python 将 100 万个数相加需
# 要多⻓时间。
# list_num = []
# for num in range(1,1000001):
#     list_num.append(num)
# print(min(list_num))
# print(max(list_num))
# print(sum(list_num))

# 通过给 range() 函数指定第三个参数来创建⼀个列
# 表，其中包含 1〜20 的奇数；再使⽤⼀个 for 循环将这些数打印出
# 来。
jishus = [jishu for jishu in range(1,20,2)]
# jishus = []
# for jishu in range(1,20,2):     
#     jishus.append(jishu) 可以用上面的推导式代替😁
for jishu in jishus:
    print(jishu)
print("\n")

# 创建⼀个列表，其中包含 3〜30 内能被 3 整除的
# 数，再使⽤⼀个 for 循环将这个列表中的数打印出来。
list_num2 = [num2 for num2 in range(3,30,3)]
print(list_num2)
for num2 in list_num2:
    print(num2)
    
# 将同⼀个数乘三次称为⽴⽅。例如，在 Python 中，2
# 的⽴⽅⽤ 2**3 表⽰。创建⼀个列表，其中包含前 10 个整数（1〜
# 10）的⽴⽅，再使⽤⼀个 for 循环将这些⽴⽅数打印出来。
cubes = [cube**3 for cube in range(1,10)]
print(f"{cubes}\n")
for cube in cubes:
    print(cube)