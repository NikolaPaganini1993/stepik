# Даны три вещественных числа a, b, c.
# Напишите программу, которая находит вещественные корни квадратного уравнения a*x**2+b*x+c=0.

from math import *

a = float(input())
b = float(input())
c = float(input())

discriminant = b ** 2 - 4 * a * c

if discriminant > 0:
    x1 = (-b - sqrt(discriminant)) / (2 * a)
    x2 = (-b + sqrt(discriminant)) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))
elif discriminant == 0:
    print(-b / (2 * a))
else:
    print("Нет корней")