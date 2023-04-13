# Напишите программу, вычисляющую значение тригонометрического выражения

from math import *

x = float(input())
r = radians(x)
result = sin(r) + cos(r) + tan(r) ** 2
print(result)
