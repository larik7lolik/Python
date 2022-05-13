# Строка содержит набор чисел. Показать большее и меньшее число Символ-разделитель - пробел

import os
os.system("cls")

str = '2356 45 5675 889 9658410 894 487 124'
print(str)

str = str.split()
str = list(map(int, str))
print(str)

print('\nМаксимальное число: ', max(str))
print('Минимальное число: ', min(str), '\n')