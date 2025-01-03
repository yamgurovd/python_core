"""
Неравенство треугольника   ⃤
Напишите программу, которая принимает три положительных числа и определяет, существует ли невырожденный треугольник с такими сторонами.

Формат входных данных
На вход программе подаются три положительных целых числа.

Формат выходных данных
Программа должна вывести «YES» или «NO» в соответствии с условием задачи.

Примечание. Треугольник существует, если выполняется неравенство треугольника:
a+b>c
a+c>b
b+c>a

link - https://stepik.org/lesson/265083/step/13?auth=registration&unit=246031
"""
a = int(input())
b = int(input())
c = int(input())

if a+b>c and a+c>b and b+c>a:
    print("YES")
else:
    print("NO")