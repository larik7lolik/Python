# Даны два файла в каждом из которых находится запись многочлена.
# Сформировать файл содержащий сумму многочленов.
from itertools import *
from task033 import get_polynomial
import os
os.system("cls")


file1 = 'task033_1.txt'
file2 = 'task033_2.txt'


def read_pol(file):  # Получение данных из файла
    with open(str(file), 'r') as data:
        pol = data.read()
    return pol


def convert_pol(pol):  # удалили "хвостик" и порезали" строку на массив , разделитель знак " + "
    pol.replace('= 0', '')
    pol = pol.split(' + ')
    pol = [i[0] for i in pol]
    for i in range(len(pol)):
        if pol[i] == 'x':
            pol[i] = '1'
    pol = pol[::-1]
    return pol


pol1 = read_pol(file1)
pol2 = read_pol(file2)
print('Исходные полиномы:')
print(pol1)
print(pol2)
print('_'*30)
print(convert_pol(pol1))
print(convert_pol(pol2))
pol1_coef = list(map(int, convert_pol(pol1)))
pol2_coef = list(map(int, convert_pol(pol2)))
print(pol1_coef)
print(pol2_coef)
print('_'*30)

sum_coef = list(map(sum, zip_longest(pol1_coef, pol2_coef, fillvalue=0)))
print(sum_coef)
sum_coef = sum_coef[::-1]
print(sum_coef)
sum_pol = get_polynomial(len(sum_coef)-1, sum_coef)
print('Итоговый результат сложения полиномов:\n', sum_pol)
with open('task034.txt', 'w') as file_sum:
    file_sum.writelines(sum_pol)