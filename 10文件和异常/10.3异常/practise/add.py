num1, num2 = 0, 0
while True:
    try:
        num1 = input("enter first number(enter q to quit):")
        if num1 == 'q':
            break
        num1 = int(num1)
    except ValueError:
        print("enter a number!")
        continue
    else:
        while True:
            try:
                num2 = input("enter second number(enter q to quit):")
                if num2 == 'q':
                    break
                num2 = int(num2)
            except ValueError:
                print("enter a number!")
                continue
            else:
                print(f"calculate result:{num1 + num2}")
                break
