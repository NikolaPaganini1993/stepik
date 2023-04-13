# На вход программе подается число n – количество собачьих лет.
# Напишите программу, которая вычисляет возраст собаки в человеческих годах.

dogage = float(input())
humanage = 0
if dogage <= 2:
    humanage = dogage * 10.5
else:
    humanage = 21 + ((dogage - 2) * 4)
print(humanage)