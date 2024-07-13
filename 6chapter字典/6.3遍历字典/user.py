
user_0 = { 
    'username': 'shuibotter', 
    'first': 'shui', 
    'last': 'cc', 
    }
 # 遍历字典 item()
for key, value in user_0.items():  
    print(f"\nKey: {key}") 
    print(f"Value: {value}") 
    
favorite_languages = { 
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'rust', 
    'phil': 'python', 
    } 
 
for name, language in favorite_languages.items(): 
    print(f"{name.title()}'s favorite language is {language.title()}.")
    
# 遍历字典中的所有键 keys()
favorite_languages = { 
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'rust', 
    'phil': 'python', 
    }   
for name in favorite_languages.keys():  # for name in favorite_languages: 同等效果
    print(name.title()) 
    
friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")        # 打印人名

    if name in friends:                 # 如果有和friends相同的人名 打印之
        language = favorite_languages[name].title()     # 给lanuage赋值
        print(f"\t{name.title()},I see you love {language}!")

if 'erin' not in favorite_languages.keys():     # key()还可以核实列表元素存在
    print("Erin, please take our poll!") 
    
# 6.3.3 按特定的顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys(),reverse=True):
    print(f"{name.title()},thank you for taking the poll.\n")
    
# 6.3.4 遍历字典中的所有值 value()
print("The following languages have been mentioned:") 
for language in favorite_languages.values(): 
    print(language.title()) 
# set()创建集合 剔除重复项
print("\nThe following languages have been mentioned:") 
for language in set(favorite_languages.values()): 
    print(language.title()) 
    
languages = {'python', 'rust', 'python', 'c'}   # 直接用花括号也可以创建集合，但是要注意别和字典弄混了