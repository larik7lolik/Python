#4. Показать первую цифру дробной части числа
import os
os.system("cls")

n = float(input('Введите дробное число: '))
d = int((n*10)% 10)
print('Первая цифра дробной части числа равна : ',d, '\n')

# number = float(input('Введите число: '))
# number1=str(float(number))
# number2 = number1.split('.')
# print(number2)
# #print(type(number1))
# number3 = number2[1]
# #print(number3)
# number_fin =number3[0]
# print((number_fin))

