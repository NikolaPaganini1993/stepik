# Вводятся 3 строки в случайном порядке.
# Напишите программу, которая выясняет можно ли из длин этих строк построить возрастающую арифметическую прогрессию.

str1 = input()
str2 = input()
str3 = input()

len1 = len(str1)
len2 = len(str2)
len3 = len(str3)

maximum = max(len1, len2, len3)
minimum = min(len1, len2, len3)
middle = len1 + len2 + len3 - maximum - minimum

if middle - minimum == maximum - middle:
    print("YES")
else:
    print("NO")