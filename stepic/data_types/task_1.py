"""
Площадь треугольника
Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь.
Формат входных данных
На вход программе подаются два действительных числа (каждое на отдельной строке) – длины катетов.

Формат выходных данных
Программа должна вывести одно число – площадь треугольника.

Подсказка - формула нахождения площади треугольника s=1/2ab
"""

a = int(input("Введите сторону треугольника а: "))
b = int(input("Введите сторону треугольника b: "))

s = 1/2*a*b
print(s)