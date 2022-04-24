# Найти расстояние между двумя точками пространства
import os
os.system("cls")

# from math import sqrt

# def find(first, second):
#     result = (second - first) * (second - first)
#     return result

# x1 = int(input('Введите координату X1' + '\n'))
# y1 = int(input('Введите координату Y1' + '\n'))
# x2 = int(input('Введите координату X2' + '\n'))
# y2 = int(input('Введите координату Y2' + '\n'))
# z1 = int(input('Введите координату X1' + '\n'))
# z2 = int(input('Введите координату Y1' + '\n'))
# sum = (find(x1, x2) + find(y1, y2)+find(z1,z2))**0.5

# print(f'Расстояние между точками в 3D пространстве = {round(sum,3)}')


import math
import random

xa = random.randrange(-10, 11)
ya = random.randrange(-10, 11)
za = random.randrange(-10, 11)
xb = random.randrange(-10, 11)
yb = random.randrange(-10, 11)
zb = random.randrange(-10, 11)

distance_between_points = round(math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2 + (zb - za) ** 2), 1)

print(f"Point a: {xa, ya, za} \nPoint b: {xb, yb, zb}")
print(f"The distance between points is {distance_between_points}.")
