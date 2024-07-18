# 练习 9.4：就餐⼈数 在为练习 9.1 编写的程序中，添加⼀个名为
# number_served 的属性，并将其默认值设置为 0。根据这个类创建⼀
# 个名为 restaurant 的实例。打印有多少⼈在这家餐馆就餐过，然后
# 修改这个值并再次打印。
# 添加⼀个名为 set_number_served() 的⽅法，⽤来设置就餐⼈
# 数。调⽤这个⽅法并向它传递新的就餐⼈数，然后再次打印这个值。
# 添加⼀个名为 increment_number_served() 的⽅法，⽤来让就餐
# ⼈数递增。调⽤这个⽅法并向它传递⼀个这样的值：你认为这家餐馆
# 每天可能接待的就餐⼈数。
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


my_restaurant = Restaurant('水家牛蛙', '辣子牛蛙')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant.set_number_served(20)
my_restaurant.show_numer_served()

my_restaurant.increment_number_served(15)
my_restaurant.show_numer_served()


# 练习 9.5：尝试登录次数在为练习 9.3 编写的 User 类中，添加⼀个
# 名为 login_attempts 的属性。编写⼀个名为
# increment_login_attempts() 的⽅法，⽤来将属性
# login_attempts 的值加 1。再编写⼀个名为
# reset_login_attempts() 的⽅法，⽤来将属性
# login_attempts 的值重置为 0。
# 根据 User 类创建⼀个实例，再调⽤
# increment_login_attempts() ⽅法多次。打印属性
# login_attempts 的值，确认它正确地递增了。然后，调⽤⽅法
# reset_login_attempts()，并再次打印属性 login_attempts
# 的值，确认它被重置为 0。
class User:
    """模拟用户信息"""

    def __init__(self, first_name, last_name, age, email):
        """初始化用户信息"""
        self.firstname = first_name
        self.lastname = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        full_name = self.firstname + self.lastname
        print("用户信息：")
        print(f"name: {full_name}")
        print(f"age: {self.age}")
        print(f"e-mail: {self.email}")

    def greet_user(self):
        full_name = self.firstname + self.lastname
        print(f"Hello, {full_name}")

    def increment_login_attempts(self):
        """将属性login_attempts 的值加 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """将属性login_attempts 的值重置为 0"""
        self.login_attempts = 0

    def show_login_attempts(self):
        """打印等登录次数"""
        print("登录次数是:")
        print(self.login_attempts)


scc = User('shui', 'cc', 12, '1259230861@qq.com')
scc.describe_user()
scc.greet_user()

scc.increment_login_attempts()
scc.show_login_attempts()

scc.reset_login_attempts()
scc.show_login_attempts()
