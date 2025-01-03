"""Разбиение на чанки 🌶️
На вход программе подаются две строки: на одной – символы, на другой – число n. Из первой строки формируется список.

Реализуйте функцию chunked(), которая принимает на вход список и число, задающее размер чанка (куска),
а возвращает список из чанков (кусков) указанной длины.

Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные символом пробела и число n на отдельной строке.

Формат выходных данных
Программа должна вывести указанный вложенный список.б

Примечание. Не забудьте вызвать функцию chunked(), чтобы вывести результат. 😀"""


def chunked(iterable, n):
    """Разбивает список на чанки заданного размера."""
    chunks = []  # Список для хранения чанков
    for i in range(0, len(iterable), n):
        # Добавляем в список чанк из n элементов
        chunks.append(iterable[i:i + n])
    return chunks


# Ввод данных
input_string = input()
n = int(input())

# Формируем список из введенной строки
elements = input_string.split()

# Вызываем функцию chunked и выводим результат
result = chunked(elements, n)
print(result)


# Второй способ решения задачи - взято из форума
def chunked(sp, n):
    return [sp[x:x + n] for x in range(0, len(sp), n)]


s = input().split()
n = int(input())
print(chunked(s, n))
