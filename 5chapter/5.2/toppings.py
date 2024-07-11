# 不等运算符(!=)
requested_topping = 'mushrooms' 
 
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# 检查特定的值是否在列表中
requested_toppings = ['mushrooms', 'onions', 'pineapple'] 


if 'mushrooms' in requested_toppings: 
     print("Adding mushrooms.") 
if 'pepperoni' in requested_toppings: 
     print("Adding pepperoni.") 
if 'extra cheese' in requested_toppings: 
     print("Adding extra cheese.") 
print("\nFinished making your pizza!")

# 总之，如果只想运⾏⼀个代码块，就使⽤ if-elif-else 语句；如果要运
# ⾏多个代码块，就使⽤⼀系列独⽴的 if 语句。