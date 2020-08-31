number = int(input("Введите целое число : "))
maximum = number % 10
while number >= 1:
    number = number // 10
    if number % 10 > maximum:
        maximum = number % 10
        continue
    else:
        print('Самая большая цифра:', maximum)
    break





