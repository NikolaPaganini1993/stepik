# Напишите программу, которая считывает натуральное число n
# и выводит первые n чисел последовательности Фибоначчи.

n = int(input())
fib1 = 1
fib2 = 1
for i in range(n):
    print(fib1, end = " ")
    fibsum = fib1 + fib2
    fib1 = fib2
    fib2 = fibsum
