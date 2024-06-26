# range() 函数
for value in range(1,5):
    print(value)
    # 注意函数只会打印1,2,3,4没有5，常见的差一行为
    # 不指定起始数的时候，默认0开始
    
# range()创建数值列表
numbers  = list(range(1,6))
print(numbers)
# range()第三个参数是步长
even_numbers = list(range(2,11,2))
print(f"步长为2：{even_numbers}")

# range()创建乘方列表
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

# max min sum
digits = []
for number in range(10):
    digit = number
    digits.append(number)
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))
