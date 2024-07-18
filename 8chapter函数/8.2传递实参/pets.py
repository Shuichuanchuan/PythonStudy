def describe_pet(pet_name, animal_type='dog'):
    """显⽰宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

describe_pet(animal_type='hamster', pet_name='harry')   # 关键字实参
# ⼀条名为 Willie 的⼩狗
describe_pet('willie')
describe_pet(pet_name='willie')

# ⼀只名为 Harry 的仓⿏
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')