from pathlib import Path

path = Path('guest_book.txt')
guest_book = ''
while True:
    guest_name = input("输入您的名字（输入q以退出）：\n")
    if guest_name == 'q':
        break
    guest_book += f"{guest_name}\n"
print(guest_book)
path.write_text(guest_book)
