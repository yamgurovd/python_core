"""Одинаковые соседи
На вход программе подается одна строка. Напишите программу, которая определяет сколько в ней одинаковых соседних символов.

Формат входных данных
На вход программе подается одна строка.

Формат выходных данных
Программа должна вывести количество одинаковых соседних символов."""
text = input()
counter = 0

for i in range(len(text) + 1):
    if text[i] == text[i + 1]:
        counter += 1

print(counter)