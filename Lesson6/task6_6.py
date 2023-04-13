# Дано положительное действительное число. Выведите его первую цифру после десятичной точки.

number = float(input())
digit = number - int(number)
firstdigit = int(digit * 10)
print(firstdigit)