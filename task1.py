# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

n = input('Введите вещественное число: ')

n = n.split('.')
my_list = []
fig = 0
summ = 0

if len(n) < 2:
    my_list = list(n[0])

elif len(n) == 2:
    my_list = list(n[0])
    my_list.append(n[1])

for i in range(len(my_list)):
    if int(my_list[i]) > 9:
        while int(my_list[i]) > 0:
            fig = int(my_list[i])%10
            my_list[i] = int(my_list[i])//10
            summ = summ+fig
    else:
        fig = int(my_list[i])
        summ = fig+summ
    
print(summ)


    



