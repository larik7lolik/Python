# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

import os
import random
os.system("cls")

def multy(a):
    if a == 1:
        return 1
    return a * multy(a-1)

n = random.randint(6,10)

for i in range(1,10):
    print(multy(i), end=' ')