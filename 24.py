# 24.	Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# •	[1.1, 1.2, 3.1, 5, 10.01] => 0.19

import os
from random import *
os.system("cls")


list = [1.1, 1.2, 3.1, 5, 10.01]  # [uniform(1, 21) for i in range(8)]
print(list, '\n')
list1 = []

for i in range(len(list)):
    if list[i] - round(list[i]) == 0:
        continue
    else:

        list1.append(round(list[i] - round(list[i]), 3))

print(list1)
print('\nМаксимальное число: ', max(list1))
print('\nМинимальное число: ', min(list1))
print('\nРазница: ', max(list1) - min(list1))





# text = input('Введите вещественное число' + '\n')
# list = text.replace(',','.') # Подстраховка на случай ввода ',' вместо '.'
# str_lst= list.split('.') # Разделение полученного списка по точке на несколько индексов
# int_lst = [int(x) for x in str_lst] # Функция конвертации строчного списка в целочисленный список на несколько индексов
# first = 0
# while (int_lst[0] != 0):
#     first = first + int_lst[0] % 10
#     int_lst[0] = int_lst[0] // 10
# # Сумма чисел слева от исходной точки




