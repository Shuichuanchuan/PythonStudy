from random import choice


def lottery_result(*numbers):
    sum1 = 0
    current_numbers = []
    while current_numbers != [7, 7, 4, 6]:
        current_numbers = []
        i = 1
        while i <= 4:
            current_numbers.append(choice(numbers))
            i += 1
            sum1 += 1
    print(current_numbers)
    print(f"您一共用了{sum1}次才中奖")


print("如果您的彩票为：7746")
lottery_result(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd')
