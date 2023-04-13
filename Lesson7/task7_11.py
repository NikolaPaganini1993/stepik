# Даны два целых числа
# Напишите программу, которая выводит все нечетные числа от m до n включительно в порядке убывания.

m = int(input())
n = int(input())
if m % 2 == 0:
    for i in range(m-1, n - 1, -2):
        print(i)
if m % 2 != 0:
    for i in range(m, n - 1, -2):
        print(i)


