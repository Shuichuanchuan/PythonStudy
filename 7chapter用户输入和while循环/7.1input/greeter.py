# input()获取输入
prompt = ("If you share your name, we can personalize the messages you"
          "see.")
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

# 使⽤ int() 来获取数值输⼊
age = input("How old are you? ")
age = int(age)
print(age >= 15)
