# На вход программе подается натуральное число n.
# Напишите программу вычисления знакочередующей суммы

n = int(input())
count = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        count = count - i
    else:
        count = count + i
print(count)