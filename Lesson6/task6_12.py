# Напишите программу определяющую манхэттенское расстояние между двумя точками, координаты которых заданы.

p1 = int(input())
p2 = int(input())
q1 = int(input())
q2 = int(input())

distance = abs(p1 - q1) + abs(p2 - q2)
print(distance)