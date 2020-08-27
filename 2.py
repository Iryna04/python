user_seconds = int(input('Введите время в секундах: '))
hour = user_seconds // 3600
remainder_hour = user_seconds % 3600
minutes = remainder_hour // 60
seconds = remainder_hour % 60
print(f'{hour}:{minutes}:{seconds}')
