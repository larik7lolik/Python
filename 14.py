# 14.	Подсчитать сумму цифр в вещественном числе.
import os
import random
os.system("cls")

num = input('Введите число:' + '\n')
a = num.split('.') # переводим в строковый тип, убираем точку
summa = sum(map(int, a)) # переводим в числовой тип, считаем сумму
print('Сумма цифр данного числа равна:', summa, '\n')


# задаем случайное вещественное число из диапазона
a = random.uniform(1, 1001)

print('Задано число:', a, '\nСумма цифр данного числа равна:', sum(
map(int, str(a).replace('.', ''))), '\n')