# Напишите программу, которая упорядочивает три числа от большего к меньшему.

num1 = int(input())
num2 = int(input())
num3 = int(input())
maximum = max(num1, num2, num3)
minimum = min(num1, num2, num3)
middle = num1 + num2 + num3 - maximum - minimum
print(maximum)
print(middle)
print(minimum)
