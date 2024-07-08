# if 
cars = ['audi', 'bmw', 'subaru', 'toyota'] 
for car in cars: 
    if car == 'bmw': 
        print(car.upper()) 
    else: 
        print(car.title())
 
# 如何在检查是否相等时忽略⼤⼩写
car = 'Audi'
car.lower() == 'audi' 
print(car)      #lower() 不会修改原来的值