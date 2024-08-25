"""
Арифметическая прогрессия
Напишите программу, которая определяет, являются ли три заданных числа (в указанном порядке) последовательными членами арифметической прогрессии.

Формат входных данных
На вход программе подаются три числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести «YES» или «NO» (без кавычек) в соответствии с условием задачи.

Формула - ( b - a) + b = c

link - https://stepik.org/lesson/265081/step/9?unit=246029
"""

digit_1 = int(input("Введите число 1: "))
digit_2 = int(input("Введите число 2: "))
digit_3 = int(input("Введите число 3: "))

if (digit_2 - digit_1) + digit_2 == digit_3:
    print("YES")
else:
    print("NO")