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
    
