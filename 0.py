# По двум заданным числам проверить является ли одно квадратом второго 
import os
os.system("cls")

num = int(input('Введите число: '))
num1 = int(input('Введите число: '))
if num1**2 == num:
    print('Второе число является')
else: 
    print('He является')


