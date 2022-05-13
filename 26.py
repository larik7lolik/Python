# 26.	Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# •	для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
#  [Негафибоначчи] 
import os
from random import *
os.system("cls")

n = randint(10, 21)
print('Задано число: ', n, '\n')


def fibo(index):
    if index == 1:
        return 0
    elif index == 2:
        return 1
    return fibo(index-1)+fibo(index-2)


list = [fibo(i) for i in range(1, n+1)]
print(list)
list = list[::-1]+list[1:]
print(list, '\n')