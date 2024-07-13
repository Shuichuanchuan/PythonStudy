responses = {}

polling_active = True    # set a flag

while polling_active:
    # 提⽰输⼊被调查者的名字和回答
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    # 将回答存储在字典中
    responses[name] = response
    repeat = input("Would you like to let another person respond?(yes / no)")
    if repeat == 'no':
        polling_active = False

# 调查结束，显⽰结果
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
