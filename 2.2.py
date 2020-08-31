count = int(input('Введите длину списка:'))
my_list = []
lenght = 0
while count > lenght:
    my_list.append(input('Введите значение елемента списка:'))
    lenght = lenght + 1
print(my_list)
if len(my_list) % 2 == 0:
    index = 0
    while index < len(my_list):
        element = my_list[index]
        my_list[index] = my_list[index + 1]
        my_list[index + 1] = element
        index = index + 2
else:
    index = 0
    while index < len(my_list) - 1:
        element = my_list[index]
        my_list[index] = my_list[index + 1]
        my_list[index + 1] = element
        index = index + 2
print(my_list)

