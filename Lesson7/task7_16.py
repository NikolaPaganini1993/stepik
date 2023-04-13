# На вход программе подается натуральное число n.
# Напишите программу, которая вычисляет значение выражения

from math import *

n = int(input())
count = 0
for i in range(1, n + 1):
    count = count + (1 / i)
    count2 = count - log(n)
print(count2)