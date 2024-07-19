from pathlib import Path
import json


def enter_number():
    number = input("输入一个你喜欢的数字：")
    path = Path('favorite_number.txt')
    contents = json.dumps(number)
    path.write_text(contents)
    return number


def get_number():
    path = Path('favorite_number.txt')
    contents = path.read_text()
    number = json.loads(contents)
    print(f"you favorite number is: {number}")


def show_number():
    path = Path('favorite_number.txt')
    if path.exists():
        contents = path.read_text()
        number = json.loads(contents)
        print(f"I know your favorite number! It's {number}.")
        return number
    else:
        number = input("输入一个你喜欢的数字：")
        path = Path('favorite_number.txt')
        contents = json.dumps(number)
        path.write_text(contents)
        print(f"你输入的数字:{number}")
        return number


show_number()
