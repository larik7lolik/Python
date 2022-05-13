# Найти корни квадратного уравнения Ax² + Bx + C = 0
# -Математикой
# -Используя дополнительные библиотеки*

from math import *
from random import *
import os
os.system("cls")

a = uniform(1, 100)
b = uniform(1, 100)
c = uniform(1, 100)
print('a = ', a)
print('b = ', b)
print('c = ', c)

discr = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discr)

if discr > 0:
    x1 = (-b + sqrt(discr)) / (2 * a)
    x2 = (-b - sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")