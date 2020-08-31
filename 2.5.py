new_element = int(input('Введите новый элемент рейтинга: '))
my_list = [9, 6, 4, 4, 1]
count = my_list.count(new_element)
for element in my_list:
    if count > 0:
        index = my_list.index(new_element)
        my_list.insert(index + count, new_element)
        break
    else:
        if new_element < my_list[len(my_list) - 1]:
            my_list.append(new_element)
            break
        elif new_element > element:
            index_1 = my_list.index(element)
            my_list.insert(index_1, new_element)
            break
print(my_list)
