# 练习 9.6：冰激凌⼩店 冰激凌⼩店是⼀种特殊的餐馆。编写⼀个名为
# IceCreamStand 的类，让它继承你为练习 9.1 或练习 9.4 编写的
# Restaurant 类。这两个版本的 Restaurant 类都可以，挑选你更喜
# 欢的那个即可。添加⼀个名为 flavors 的属性，⽤于存储⼀个由各种
# ⼝味的冰激凌组成的列表。编写⼀个显⽰这些冰激凌⼝味的⽅法。创
# 建⼀个 IceCreamStand 实例，并调⽤这个⽅法。
class Restaurant:
    """模拟一家餐厅"""

    def __init__(self, restaurant_name, cuisine_type):
        """ 初始化餐厅属性"""
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_serverd = 0

    def describe_restaurant(self):
        """显示餐厅的名称和菜品"""
        print(f"餐厅的名字叫做{self.name}")
        print(f"餐厅的菜品有：{self.type}")

    def open_restaurant(self):
        """正在营业"""
        print(f"{self.name}餐厅正在营业")

    def set_number_served(self, numbers):
        """设置就餐人数"""
        self.number_serverd = numbers

    def show_numer_served(self):
        """显示就餐人数"""
        print(f"就餐人数：{self.number_serverd}")

    def increment_number_served(self, numbers):
        self.number_serverd += numbers


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        """继承Restaurant"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['牛肉', '臭豆腐', '咸菜']

    def show_flavors(self):
        """显示冰淇淋风味列表"""
        print("风味列表：")
        for flavor in self.flavors:
            print(flavor)


my_icecream_stand = IceCreamStand('水的冰淇淋', '冰淇淋')
my_icecream_stand.show_flavors()
