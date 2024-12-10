"""k-ая буква слова 🌶️
На вход программе подается натуральное число n и n строк, а затем число k.
Напишите программу, которая выводит k-ую букву из введенных строк на одной строке без пробелов.

Формат входных данных
На вход программе подается натуральное число n,  далее n строк, каждая на отдельной строке.
В конце вводится натуральное число k – номер буквы (нумерация начинается с единицы).

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Если некоторые строки слишком короткие, и в них нет символа с заданным номером,
то такие строки при выводе нужно игнорировать.
"""

n = int(input())
li = []
for _ in range(n):
    li.append(input())
index = int(input())
res = ''
for s in li:
    if len(s) >= index:
        res += s[index - 1]

print(res)

# Второй способ решения задачи - взято из форума
data = [input() for i in range(int(input()))]
k = int(input())
for i in data:
    if len(i) >= k:
        print(i[k - 1], end='')

# Третий способ решения задачи - взято из Гигачата
# Чтение входных данных
n = int(input())  # Количество строк
strings = [input().strip() for _ in range(n)]  # Список строк
k = int(input())  # Позиция буквы

# Сбор k-ой буквы из каждой строки
result = ''.join([s[k - 1] for s in strings if len(s) >= k])

# Вывод результата
print(result)