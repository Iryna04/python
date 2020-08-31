my_str = input('Введите слова через пробел:')
words = my_str.split()
for ind, el in enumerate(words, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f'{ind}. {el}')
