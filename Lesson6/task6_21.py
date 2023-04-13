# Напишите программу определяющую евклидово расстояние между двумя точками, координаты которых заданы.

from math import sqrt

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print(distance)
