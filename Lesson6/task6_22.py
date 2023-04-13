# Напишите программу определяющую площадь круга и длину окружности по заданному радиусу R.
from math import pi

r = float(input())

s = pi * (r ** 2)
c = 2 * pi * r

print(s)
print(c)
