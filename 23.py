# 23.	Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый
#  и последний элемент, второй и предпоследний и т.д.
# Пример:
# •	[2, 3, 4, 5, 6] => [12, 15, 16];
# •	[2, 3, 5, 6] => [12, 15]

# Первый способ:
# import math


# def pair_multiply(array):
#     length = len(array)
#     result = []
#     for i in range(0, math.ceil(length/2)):
#         result.append(array[i]*array[length-1-i])
#     return result

# Второй способ:
# list_of_numbers = [2, 3, 4, 5, 6]

# print('Исходный список: ')
# print(f'{list_of_numbers}\n\n')
# print('Список полученный произведением пар чисел: ')
# print(f'{pair_multiply(list_of_numbers)}\n\n')

# Третий способ:
list = [2, 3, 4, 5, 6]
print(list)
list1 = []

for i in range ((len(list) + 1) // 2):
    list1.append(list[i] * list[-1-i]) # индекс элемента * на самый крайний последний элемент
print(list1)


    


