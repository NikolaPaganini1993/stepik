# Даны названия трех городов.
# Напишите программу, которая определяет самое короткое и самое длинное название города.

sity1 = input()
sity2 = input()
sity3 = input()

len1 = len(sity1)
len2 = len(sity2)
len3 = len(sity3)

minimum = min(len1, len2, len3)
maximum = max(len1, len2, len3)


if minimum == len(sity1):
    print(sity1)
if minimum == len(sity2):
    print(sity2)
if minimum == len(sity3):
    print(sity3)

if maximum == len(sity1):
    print(sity1)
if maximum == len(sity2):
    print(sity2)
if maximum == len(sity3):
    print(sity3)
