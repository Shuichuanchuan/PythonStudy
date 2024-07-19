from car import Car


class Battery:
    """⼀次模拟电动汽⻋电瓶的简单尝试"""

    def __init__(self, battery_size=40):
        """初始化电池的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印⼀条描述电池容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """打印⼀条描述电池续航⾥程的消息"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """模拟电动汽⻋的独特之处"""

    def __init__(self, make, model, year):
        """
        先初始化⽗类的属性，再初始化电动汽⻋特有的属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()