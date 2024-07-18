# 练习 9.1：餐馆 创建⼀个名为 Restaurant 的类，为其
# __init__() ⽅法设置两个属性：restaurant_name 和
# cuisine_type。创建⼀个名为 describe_restaurant() 的⽅法
# 和⼀个名为 open_restaurant() 的⽅法，其中前者打印前述两项信
# 息，⽽后者打印⼀条消息，指出餐馆正在营业。
# 根据这个类创建⼀个名为 restaurant 的实例，分别打印其两个属
# 性，再调⽤前述两个⽅法。

class Restaurant:
    """模拟一家餐厅"""

    def __init__(self, restaurant_name, cuisine_type):
        """ 初始化餐厅属性"""
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        """显示餐厅的名称和菜品"""
        print(f"餐厅的名字叫做{self.name}")
        print(f"餐厅的菜品有：{self.type}")

    def open_restaurant(self):
        """正在营业"""
        print(f"{self.name}餐厅正在营业")


my_restaurant = Restaurant('水家牛蛙', '辣子牛蛙')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()


class User:
    """模拟用户信息"""

    def __init__(self, first_name, last_name, age, email):
        """初始化用户信息"""
        self.firstname = first_name
        self.lastname = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        full_name = self.firstname + self.lastname
        print("用户信息：")
        print(f"name: {full_name}")
        print(f"age: {self.age}")
        print(f"e-mail: {self.email}")

    def greet_user(self):
        full_name = self.firstname + self.lastname
        print(f"Hello, {full_name}")


sccuser = User('shui', 'cc', 12, '1259230861@qq.com')
sccuser.describe_user()
sccuser.greet_user()