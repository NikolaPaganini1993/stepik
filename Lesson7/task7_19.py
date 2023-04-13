# Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.

count = 1
for i in range(10):
    number = int(input())
    if number != 0:
        count = count * number
print(count)

