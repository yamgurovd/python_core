"""В столбик 1
На вход программе подается одна строка. Напишите программу, которая выводит элементы строки с индексами
0, 2, 4, ... в столбик.

Формат входных данных
На вход программе подается одна строка.

Формат выходных данных
Программа должна вывести элементы строки с индексами 0, 2, 4, ..., каждое на отдельной строке."""
text = input()

for i in range(0, len(text), 2):
    print(text[i])