# 元组 元组的元素是不可以修改的
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
# 遍历元组
for dimension in dimensions: 
    print(dimension) 
    
# 修改元组变量,虽然不能修改元组的元素，但可以给表⽰元组的变量赋值
dimensions = (400, 100) 
print("\nModified dimensions:") 
for dimension in dimensions: 
    print(dimension) 
    
# 有⼀家⾃助式餐馆，只提供 5 种简单的⾷品。请
# 想出 5 种简单的⾷品，并将其存储在⼀个元组中。
foods = ('青椒肉丝','西红柿蛋花汤','鱼香肉丝','烤包子','糖醋排骨')
for food in foods:
    print(food)    
# foods[1] = '水煮肉片' 
# 尝试修改
foods = ('\n青椒肉丝','西红柿蛋花汤','水煮肉片','烤包子','孜然羊肉')
for food in foods:
    print(food)  