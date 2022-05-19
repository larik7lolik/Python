# 41.	Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#  Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример:
# На сжатие:
# Входные данные:
# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Выходные данные: 
# 12W1B12W3B24W1B14W

# Сжатие файла:
import os
os.system("cls")


with open('task41_1.txt', 'r') as data:
    my_text = data.read()
    
def encode_rle(string):   # кодировка
    str_code = ''
    count = 1
    for i in range(len(string)):
        if i <= len(string)-1:
           if string[i] == string[i + 1]:
            count += 1
           else:
            a = string[i]
            str_code += str(count) + string[i]
            count = 1
        else:
         str_code += str(count) + string[i]
    return str_code

# кодировка
str_code = encode_rle(my_text)
print('Исходный текст: ', my_text)
print('Обработанный текст: ', str_code, '\n')
#сохраняем в файл:
with open('task41_2.txt', 'r') as data:
   my_text2 =  data.read()


# восстановления данных:

def decoding_rle(string):
    str_decode = ''
    count = ''
    for char in string:
        if char.isdigit():     
            count =+ char
    else:
        str_decode += char * int(count)
        count = ''
    return  str_decode 


str_decode = decoding_rle(my_text2)       
print('Исходный текст: ', my_text2)
print('Обработанный текст: ', str_decode, '\n')




