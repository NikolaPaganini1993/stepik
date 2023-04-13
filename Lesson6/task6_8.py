# Напишите программу, которая находит наименьшее и наибольшее из пяти чисел.

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())
max = max(num1, num2, num3, num4, num5)
min = min(num1, num2, num3, num4, num5)

print(f"Наименьшее число = {min}")
print(f"Наибольшее число = {max}")
