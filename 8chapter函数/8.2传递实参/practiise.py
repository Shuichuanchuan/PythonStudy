# 练习 8.3：T 恤 编写⼀个名为 make_shirt() 的函数，它接受⼀个
# 尺码以及要印到 T 恤上的字样。这个函数应该打印⼀个句⼦，简要地
# 说明 T 恤的尺码和字样。
def make_shirt(size='big', font_type='I love Python'):
    print(f"T恤的尺码是{size}，图案是{font_type}")


def describe_city(city_name='Reykjavik', nation='Iceland'):
    print(f"{city_name.title()} is in {nation.title()}")


make_shirt('m', 'flower')
make_shirt(size='m', font_type='flower')

make_shirt()
make_shirt(size='m')
make_shirt(font_type='you love me')

# 练习 8.5：城市 编写⼀个名为 describe_city() 的函数，它接受
# ⼀座城市的名字以及该城市所属的国家。这个函数应该打印⼀个像下
# ⾯这样简单的句⼦。
describe_city(city_name='Beijing',nation='china')
