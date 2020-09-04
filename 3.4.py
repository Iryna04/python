x = int(input('Введите положиттельное число: '))
y = int(input('Введите отрицательное число: '))
def step(x, y):
    degree = x ** y
    print(degree)


step(x, y)

x_1 = int(input('Введите положиттельное число: '))
y_1 = int(input('Введите отрицательное число (без минуса): '))
def my_func(x_1, y_1):
    count = 1
    while count < y_1:
        x_1 = x_1 * x_1
        count = count + 1
    degree_1 = 1 / x_1
    print(degree_1)


my_func(x_1, y_1)
