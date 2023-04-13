# Назовем число интересным, если в нем разность максимальной и минимальной цифры равняется
# средней по величине цифре. Напишите программу, которая определяет интересное число или нет.
# Если число интересное, следует вывести – «Число интересное» иначе «Число неинтересное».

number = int(input())
num1 = number // 100
num2 = number // 10 % 10
num3 = number % 10
maximum = max(num1, num2, num3)
minimum = min(num1, num2, num3)
middle = num1 + num2 + num3 - maximum - minimum
if maximum - minimum == middle:
    print("Число интересное")
else:
    print("Число неинтересное")