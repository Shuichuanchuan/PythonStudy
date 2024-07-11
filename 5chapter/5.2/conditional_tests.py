# 检查两个字符串是否相等和不等。
words1 = 'hello'
words2 = 'Hello'
print("words1 = words2?")
print(words1 == words2)
print("words1 != words2?")
print(words1 != words2)
# 使⽤ lower() ⽅法的条件测试。
print("words1 = words2?")
print(words1.lower() == words2.lower())

# 涉及相等、不等、⼤于、⼩于、⼤于等于和⼩于等于的数值⽐较。
num1 = 20
num2 = 13
num3 = 21
print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)
# 使⽤关键字 and 和 or 的条件测试。
print(num1 > num2 and num1 > num3)
print(num1 > num2 or num1 > num2)

# 检查测试特定的值是否在列表中。
# 测试特定的值是否不在列表中。
name_list = ['shui','li','zhou','wang']
name = 'wu'
if name in name_list:
    print("you are in the list")
if name not in name_list:
    print("you are not in")