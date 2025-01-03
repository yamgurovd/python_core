"""Произведение чисел
Напишите программу для определения, является ли число произведением двух чисел из данного набора.
Программа должна выводить результат в виде ответа «ДА» или «НЕТ».

Формат входных данных
В первой строке подаётся натуральное число n(0<n<1000) – количество чисел в наборе.
В последующих n строках вводятся целые числа, составляющие набор (могут повторяться). З
атем следует целое число, которое является или не является произведением двух каких-то чисел из набора.

Формат выходных данных
Программа должна вывести «ДА» или «НЕТ» в соответствии с условием задачи.

Примечание 1. Само на себя число из набора умножиться не может. Другими словами,
два множителя должны иметь разные индексы в наборе.

Примечание 2. Для решения задачи используйте вложенные циклы."""

n = int(input())

nums = [int(input()) for _ in range(n)]

target = int(input())

found = False

for i in range(n):
    for j in range(i + 1, n):
        if nums[i] * nums[j] == target:
            found = True
            break
        if found:
            break

if found:
    print("ДА")
else:
    print("НЕТ")

# Второй способ решения задачи - взято из форума
numbers, multiply = [int(input()) for i in range(int(input()))], int(input())
for i in range(len(numbers)-1):
    for j in range(i+1, len(numbers)):
        if multiply == numbers[i] * numbers[j]:
            exit(print("ДА"))
print("НЕТ")