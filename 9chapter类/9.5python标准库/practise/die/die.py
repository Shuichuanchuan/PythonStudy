from random import randint


class Die:
    """骰子"""

    def __init__(self, side):
        """初始化面数"""
        self.sides = 6      # 默认面数
        self.side = side    # 记录输入的面数

    def roll_die(self):
        """掷骰子"""
        self.sides = randint(1, self.side)
        print(self.sides)


print("6面的：")
i = 1
die6 = Die(6)
while i <= 10:
    die6.roll_die()
    i += 1
print("10面的：")
i = 0
die10 = Die(10)
while i <= 10:
    die10.roll_die()
    i += 1

print("20面的：")
i = 0
die20 = Die(20)
while i <= 10:
    die20.roll_die()
    i += 1
