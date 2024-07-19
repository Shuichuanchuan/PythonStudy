from car import Car, ElectricCar    # 导入多个类
import car  # 导入整个模块
my_mustang = car.Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
my_leaf = car.ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
