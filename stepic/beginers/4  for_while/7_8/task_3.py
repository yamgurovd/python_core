"""Таблица-3
Дано натуральное число n (n≤ 9). Напишите программу, которая печатает таблицу сложения для всех
чисел от 1 до n (включительно) в соответствии с примером.

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести таблицу сложения для всех чисел от 1 до n.

Примечание 1. Таблицу сложения подразумеваем от 1 до 9 (включительно).

Примечание 2. В конце строки может быть пробел."""
n = int(input())

for i in range(1, n + 1):
    print()
    for j in range(1, 10):
        print(f"{i} + {j} = {i + j}")


"""# Считываем число и записываем в переменную "n"
# Создаем цикл от 1 до считываемого числа включительно назовем его "i"
# Создаем внутренний от 1 до 9 включительно назовем его "j"
# Выводим i знак плюс j знак равно и плюсуем i + j
# Разобъем все пустым принтом"""