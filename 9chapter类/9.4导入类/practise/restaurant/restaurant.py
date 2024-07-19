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
