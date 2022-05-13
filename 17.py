# Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число

# import os
# import random
# os.system("cls")

# n = int(input())
# list = [-3, -2, -1, 0, 1, 2, 3]
# with open('file.txt', 'w')as data:
#     data.write('1\n')
#     data.write('2\n')
#     data.write('3\n')
#     data.write('4\n')
#     data.write('5\n')
#     data.write('6\n')
#     data.write('7\n')

# #exit()
# # Чтение файла
# path = 'file.txt'
# data = open(path,'r')
# for line in data:
#     print(line)
# print()
# P = list[0]*list[1]*list[2]*list[4]*list[5]*list[6]
# print(P)
# #data.cloes()
# Второй способ решения

# dots = int(input('Введите значение для крайних точек: '))

# elements = []
# mult = 1
# f = open('File.txt', 'r')

# for i in range (-dots, dots + 1):
#     elements.append(i)

# print(elements)

# for line in f:
#     mult = mult * int(elements[int(line)])

# print(mult)
# f.close() 
# Третий способ:

# n=int(input('Введите N (целое число), значение до которрого будет формироваться список: '))
# pos=input(f'Введите, через запятую, позиции элементов которые необходимо перемножить, не более {n*2}: ').split(',')

# with open('positions.txt', 'w') as positions:   
# for i in pos:                                    # считывание списка и запись в файл
# positions.write(f'{i}\n')                        #

# spisok=[]                                       # формируем список 
# step = 1
# start = -n
# stop = n+1
# if n < 0:
# step = -1
# stop -= 2
# for i in range(start, stop, step):
# spisok.append(i)

# print(spisok)

# multiply=1

# with open('positions.txt', 'r') as positions:  # считывание из файла
# for element in positions:
# multiply*=spisok[int(element.strip())]

# print(f'Произведение элементов с введенными позициями равно {multiply}')

with open('file.txt','r') as F: 
    v = []                         # числа из текстового файла записываем в массив
    for x in F:
        v.append(int(x))
    print(v)
# или так:
with open('file.txt','r') as F:
    v = [int(x) for x in F]
print(v)
