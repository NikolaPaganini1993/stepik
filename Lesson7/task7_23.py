# Напишите программу, которая считывает последовательность из 10 целых чисел
# и определяет является ли каждое из них четным или нет.

count = 0
for i in range(10):
    num = int(input())
    if num % 2 == 0:
        count = count + 1
if count != 10:
    print("NO")
else:
    print("YES")