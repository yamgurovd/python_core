"""
Интересное число
Назовём число интересным, если в нём разность максимальной и минимальной цифры равняется средней по величине цифре.
Напишите программу, которая определяет, интересное число или нет.
Если число интересное, следует вывести «Число интересное», иначе – «Число неинтересное».

Формат входных данных
На вход программе подается целое трёхзначное число.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Подсказка
1. Вводим трёхзначное число(1 переменная).
2. Делим его на 100(2 переменная).
3. Потом делим на 10 и % тоже на 10(3 переменная).
4. И ещё раз % на 10(4 переменная).
5. Уже условие ставим, если сумма (2,3,4 переменной) равна 2 * max(2,3,4 переменной) то вывести "Число интересное", если нет то "Число неинтересное"
"""

dig = int(input())
# print(dig//100)
# print(dig%100//10)
# print(dig%10)

dig_mx = max(dig // 100, dig % 100 // 10, dig % 10)
dig_mn = min(dig // 100, dig % 100 // 10, dig % 10)
dig_mdl = (dig // 100 + dig % 100 // 10 + dig % 10 - dig_mx - dig_mn)
print(dig_mn, dig_mdl, dig_mx, sep="\n")


if dig_mn + dig_mdl + dig_mx == 2 * max(dig_mn, dig_mdl, dig_mx):
    print("Число интересное")
else:
    print("Число неинтересное")

# if dig_mx - dig_mn == dig_mdl:
#     print("")