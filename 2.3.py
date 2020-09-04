month = int(input('Введите месяц в виде целого числа: '))
season_dict = {'winter': 'Зима', 'spring': 'Весна', 'summer': 'Лето', 'autumn': 'Осень'}
if month == 1 or month == 2 or month == 12:
    print(season_dict.get('winter'))
elif month == 3 or month == 4 or month == 5:
    print(season_dict.get('spring'))
elif month == 6 or month == 7 or month == 8:
    print(season_dict.get('summer'))
elif month == 9 or month == 10 or month == 11:
    print(season_dict.get('autumn'))
else:
    print('Вы ввели неверное число.')
season_list = ['Зима', 'Весна', 'Лето', 'Осень']
if month == 1 or month == 2 or month == 12:
    print(season_list[0])
elif month == 3 or month == 4 or month == 5:
    print(season_list[1])
elif month == 6 or month == 7 or month == 8:
    print(season_list[2])
elif month == 9 or month == 10 or month == 11:
    print(season_list[3])
else:
    print('Вы ввели неверное число.')
