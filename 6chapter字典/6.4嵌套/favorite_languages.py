favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
}


for name, languages in favorite_languages.items():
    if len(favorite_languages[name]) == 1:  # 判断喜欢额语言是否为1门
        for language in languages:
            print(f"{name}'s favorite language is {language}")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
