# Найти максимальное из пяти чисел
import os
os.system("cls")

list = [2, 5, 65, 92, 4]
print(list)
print('Максимальное число: ', max(list)) # 1 способ

max = list[0]
for i in list:
    if i > max:
        max = i
print('Максимальное число: ',max, '\n') # 2 способ
