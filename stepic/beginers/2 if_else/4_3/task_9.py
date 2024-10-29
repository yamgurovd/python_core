"""
Пересечение отрезков 🌶️🌶️
На числовой прямой даны два отрезка:
[a1;b1][a1;b1] и [a2; b2][a2; b2]. Напишите программу, которая находит их пересечение.

Пересечением двух отрезков может быть:


Формат входных данных
На вход программе подаются четыре целых числа
a1,b1,a2,b2, каждое на отдельной строке. Гарантируется, что a1<b1 и  a2<b2.

Формат выходных данных
Программа должна вывести на экран границы отрезка, являющегося пересечением, либо общую точку, либо текст «пустое множество».
е рассматривайте все случаи буквально. Если отрезок [a2;b2] левее (хотя бы своим левым концом) отрезка [a1;b1]
то поменяйте отрезки местами. Дальше вы работаете только со случаями, где отрезок [a1;b1]гарантированно левее
(хотя бы своим левым концом) отрезка [a2;b2]:
"""

a1, b1 = int(input()), int(input())
a2, b2 = int(input()), int(input())

if b1 < a2 or b2 < a1:
    print("пустое множество")
elif b1 == a2:
    print(a2)
elif b2 == a1:
    print(a1)
elif a2 > a1 and b1 < b2:
    print(a2, b1)
elif a2 < a1 and b1 > b2:
    print(a1, b2)
elif a1 >= a2 and b2 >= b1:
    print(a1, b1)
elif a1 <= a2 and b2 <= b1:
    print(a2, b2)