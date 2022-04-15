#Вывести на экран числа от -N до N
import os
os.system("cls")

num = abs(int(input()))
for i in range (-num, num+1):
    print(i, end=' ') 


