import random

def fill_list(n = 10, min_value = 0, max_value = 100): 
    new_list = [random.randint(min_value, max_value)]
    for i in range(1, n):
        new_list.append(random.randint(min_value, max_value))
        i += 1
    return new_list

def shuffling_list(user_list):
    for i in range(len(user_list)-1, 0, -1):
        j = random.randint(0, i + 1)
        user_list[i], user_list[j] = user_list[j], user_list[i]
    return user_list

n = int(input('Количество элементов списка: '))
min_value = int(input('Граница 1 диапазона значений элементов списка: '))
max__value = int(input('Граница 2 диапазона значений элементов списка: '))
if max__value < min_value:
    max__value, min_value = min_value, max__value
source_list = fill_list(n, min_value, max__value)
print(source_list)
mixed_list = shuffling_list(source_list)
print(mixed_list)