first_number = int(input('Введите делимое число: '))
second_number = int(input('Введите делитель: '))
def division (number_1, number_2):
    if number_2 == 0:
        print('Ошибка. Делить на ноль нельзя')
    else:
        divis = number_1 / number_2
        print(divis)
division(first_number, second_number)