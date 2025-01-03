"""Задача Иосифа Флавия 🌶️🌶️
n человек, пронумерованных числами от 1 до n, стоят в кругу.
Они начинают считаться, каждый k-й по счету человек выбывает из круга,
после чего счет продолжается со следующего за ним человека. Напишите программу,
определяющую номер человека, который останется в кругу последним.

Формат входных данных
На вход программе подаются два числа n и k, записанные на отдельных строках.

Формат выходных данных
Программа должна вывести одно число – номер человека, который останется в кругу последним.

Примечание 1. Подробнее ознакомиться с классической задачей Иосифа Флавия можно по ссылке.

Примечание 2. Визуализацию работы алгоритма можно посмотреть по ссылке."""

# Считываем входные данные
n = int(input().strip())
k = int(input().strip())

# Инициализируем последний оставшийся человека
last_person = 0  # Считаем от 0

# Итеративно вычисляем последнего оставшегося
for i in range(2, n + 1):
    last_person = (last_person + k) % i

# Номер последнего человека (из 1-indexed)
print(last_person + 1)

# Второй способ решения - взято из форума
n = int(input())
k = int(input())

res = 0
for i in range(1, n + 1):
    res = (res + k) % i
print(res + 1)
