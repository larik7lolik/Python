# Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число

# Первый способ:

# N = int(input('Введите число: ' + '\n'))
# list = [i for i in range(-N,N+1)]
# path = '17.txt'
# data = open(path,'r')
# count = 1
# for line in data:
#    if int(line) > len(list)-1:
#       count*=1
# else:
#      count *= list[int(line)]
# print(count)
# data.close()




# Второй способ:

from functools import reduce
import os
import random
os.system("cls")

n = random.randint(16, 26)

list = [i for i in range(-n, n+1)]

print('Задан список: ', list, '\n')

with open('task017.txt', 'w') as data: # случайным образом задаем позиции и записываем в файл
   for i in range(int(n/2)):
       data.write(f'{random.randint(0, n*2)}\n')

def read2list(file): # читает в список из файла
    with open(file, 'r') as file:
         position_index = [int(line.strip()) for line in file.readlines()]
         position_index.sort()
         print('Выбраны позиции с индексами: \t', *position_index)
         return position_index
































position_index = read2list('task017.txt')
position_element = [list[i] for i in position_index]
mult = reduce((lambda x, y: x*y), position_element)

print('Элементы на указанных позициях:\t', *position_element,
'\nИх произведение равно : \t', mult, '\n')