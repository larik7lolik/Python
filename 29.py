# Найти наименьшее общее кратное двух чисел

import os
from random import *
os.system("cls")

a = randint(10, 100)
b = randint(10, 100)
print('a = ', a)
print('b = ', b)

for i in range(a*b, 1, -1):
    if i % a == 0 and i % b == 0:
        nok = i

print('НОК = ', nok, '\n')