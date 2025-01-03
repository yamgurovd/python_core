"""Строковые минимум и максимум
На вход программе подается последовательность строк, каждая строка на отдельной строке. Концом последовательности
является слово «КОНЕЦ» (без кавычек). При этом само слово «КОНЕЦ» не входит в последовательность,
лишь символизируя ее окончание. Напишите программу, которая находит в данной последовательности максимальную и
минимальную строки (в лексикографическом порядке) и выводит их в следующем формате:

Минимальная строка ⬇️: <минимальная строка>
Максимальная строка ⬆️: <максимальная строка>
Формат входных данных
На вход программе подается последовательность строк, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Не только у чисел мы можем находить максимум и минимум. 🤪"""
words = []

while True:
    word = input()
    if word == 'КОНЕЦ':
        break
    words.append(word)

min_word = min(words)
max_word = max(words)

print(f"Минимальная строка ⬇️: {min_word}")
print(f"Максимальная строка ⬆️: {max_word}")
