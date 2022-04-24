# Задать список из n чисел последовательности (1+1n)n 
# и вывести на экран их сумму

import os
import random
os.system("cls")

n = random.randint(6,16)
print(n)

massive = []

for i in range(1, n+1):
    massive.append(1+(1/i)**i)
print(f'{sum(massive):.2f}')

# print(f"last element {multy(n)}") # позволяет посчитать за сколько времени выполняется код

# import math   # Библиотека импортирует математические функции
# a = math.factorial(5)  # факториал
# print(a)
