# 38.	Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Пример:
# Входные данные:
#  'ываабв лповап абвцукв алоабвабв ываываыв'
# Входные данные: 
# 'лповап ываываыв'

text = 'ываабв лповап абвцукв алоабвабв ываываыв'
#print(type(text))
print(text[:])
text = text[6:13] + text[31:]
print(text)






