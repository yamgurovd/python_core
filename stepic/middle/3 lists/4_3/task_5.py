"""Треугольник Паскаля 2
На вход программе подается натуральное число n.
Напишите программу, которая выводит первые n строк треугольника Паскаля.

Формат входных данных
На вход программе подается число n (n≥1).

Формат выходных данных
Программа должна вывести первые n строк треугольника Паскаля, каждую на отдельной строке в соответствии с образцом."""
n = int(input())
lst = []

for i in range(n):
   row = [1] * (i+1)
   for j in range(i + 1):
       if j != 0 and j != i:
           row[j] = lst[i - 1][j-1] + lst[i - 1][j]
   lst.append(row)

for i in lst:
    print(*i)