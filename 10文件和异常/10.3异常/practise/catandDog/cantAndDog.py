from pathlib import Path

path_cat = Path('cat.txt')
path_dog = Path('dog.txt')

try:
    print(path_cat.read_text())
except FileNotFoundError:
    print(f"file {path_cat} not found!")

try:
    print(path_dog.read_text())
except FileNotFoundError:
    print(f"file {path_dog} not found!")
