first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
third_number = int(input('Введите третие число: '))
def my_func (number_1, number_2, number_3):
        if number_1 > number_2 > number_3:
            print(number_1, number_2)
        elif number_1 > number_2 < number_3:
            print(number_1, number_3)
        elif number_1 == number_2 == number_3:
            print('Все числа одинаковые')
        elif number_1 == number_2 and number_2 > number_3:
            print(number_1,number_2)
        elif number_2 == number_3 and number_2 > number_1:
            print(number_3,number_2)
        elif number_1 == number_3 and number_1 > number_2:
            print(number_1,number_3)
        elif number_1 == number_2 and number_2 < number_3:
            print(number_3, ', остальные два числа меньше даного и являються равными')
        elif number_2 == number_3 and number_2 < number_1:
            print(number_1, ', остальные два числа меньше даного и являються равными')
        elif number_1 == number_3 and number_1 < number_2:
            print(number_2, ', остальные два числа меньше даного и являються равными')

my_func(first_number, second_number, third_number)
