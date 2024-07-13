# 练习 7.1：汽⻋租赁 编写⼀个程序，询问⽤户要租什么样的汽⻋，并
# 打印⼀条消息，如下所⽰。
car = input("你想要什么牌子的车: ")
print(f"让我来找一下{car}")

# 练习 7.2：餐馆订位 编写⼀个程序，询问⽤户有多少⼈⽤餐。如果超
# 过 8 个⼈，就打印⼀条消息，指出没有空桌；否则指出有空桌。
customers = input("您好，请问有几个人用餐呢")
customers = int(customers)
if customers > 8:
    print("不好意思，没有这么多个人的桌位了")
else:
    print("好的，这里还有桌位")
print("\n")
# 练习 7.3：10 的整数倍 让⽤户输⼊⼀个数，并指出这个数是否是 10的整数倍。
integer = input("请输入一个数字，让我来判断是否为整数： ")
integer = int(integer)
if integer % 10 == 0:
    print(f"{integer}是10的整数倍")
else:
    print(f"{integer}不是10的整数倍")
