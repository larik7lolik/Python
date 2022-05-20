# 11.	Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

import os
from typing import Dict
os.system("cls")

# def fib(n):
#     if n in [0,1]:
#         return 1
#     else:
#         return fib(n-1)*-3

# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)

list = [(-3)**num for num in range(int(input('Введите количество элементов: ')))]

print(list)
