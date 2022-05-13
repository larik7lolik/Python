# Реализовать алгоритм перемешивания списка.
import os
import random
os.system("cls")

#list = [random.randint(1, 101) for item in range(10)]  # задали список рандомом случайных чисел от 0 до 9 элементов
list = [12,45,65,89,4,5,1]
print(list)
random.shuffle(list)      # перемешали числа
print(list, '\n')


# Реализовать алгоритм перемешивания списка. 

from random import randint

array = [1,2,3,4,5,6,7,8,9,10]
print(f'На входе имеем массив:\n{array}')
for i in range(0,len(array)-1):
    swap=array[i]
    rnd=randint(i+1,len(array)-1)
    array[i]=array[rnd]
    array[rnd]=swap
print(f'После перемешивания имеем массив:\n{array}')
