# Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

n = int(input('Введите n: '))
list_n = []
summ = 0


for i in range(1, n+1):
    list_n.append(round(((1+1/i)**i), 2))
    summ = summ + i

# while len(list_n) < n+1:
#     list_n.append((1+1/n)**n)  
#     n = list_n[len(list_n)-1]
#     summ = summ + n

print(list_n)
print(summ)
