# Программа должна вывести 4 числа – среднее арифметическое, геометрическое, гармоническое и квадратичное.

from math import sqrt

a = float(input())
b = float(input())

arithmeticMean = (a + b) / 2
geometricMean = sqrt(a * b)
harmonicMean = (2 * a * b) / (a + b)
rootMeanSquare = sqrt((a ** 2 + b ** 2) / 2)
print(arithmeticMean)
print(geometricMean)
print(harmonicMean)
print(rootMeanSquare)