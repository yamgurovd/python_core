"""Построчный вывод
На вход программе подается строка текста. Напишите программу, которая выводит слова введенной строки в столбик.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи."""
text = list(input().split())

for i in text:
    print(i)

# Второй способ решенеия
text = input()
words = text.split()
for i in range(len(words)):
    print(words[i])

# Третий способ решения - взято из форума
print(*input().split(), sep='\n')