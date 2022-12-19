
# Реализуйте алгоритм перемешивания списка. 
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для и получения случайного 
# int

import random
list_first = []
n = int(input("Введите количество элементов списка: "))

for i in range(n):
    a = int(input(f'Введите {i} элемент списка: '))
    list_first.append(a)

list_second = list(list_first)
j = 0

print(list_first)

for i in range(len(list_second)):
    j = random.randint(0,len(list_first)-1)
    list_second[i] = list_first[j]
    list_first.pop(j)

print(list_second)