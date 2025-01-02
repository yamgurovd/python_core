"""Побочная диагональ
На вход программе подается натуральное число n.
Напишите программу, которая создает матрицу размером n×n и заполняет ее по следующему правилу:

числа на побочной диагонали равны 1;
числа, стоящие выше этой диагонали, равны 0;
числа, стоящие ниже этой диагонали, равны 2.
Полученную матрицу выведите на экран. Числа в строке разделяйте одним пробелом.

Формат входных данных
На вход программе подается натуральное число n – количество строк и столбцов в матрице.

Формат выходных данных`
Программа должна вывести матрицу в соответствии с условием задачи.

Примечание. Побочная диагональ – это диагональ, идущая из правого верхнего в левый нижний угол матрицы."""

n, mtx = int(input()), []

for i in range(n):
    row = []

    for j in range(n):

        if i + j == n - 1:
            row.append(1)
        elif i + j < n - 1:
            row.append(0)
        else:
            row.append(2)

    mtx.append(row)

for row in mtx:
    print(" ".join(map(str, row)))

# ВТорой способ решения задачи - взято из форума
n = int(input())
matrix = [[sum((i > n - j - 1, i >= n - j - 1)) for j in range(n)] for i in range(n)]
[print(*row) for row in matrix]
