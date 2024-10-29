"""
Корректный email 📧
Будем считать email адрес корректным, если в нём есть символы собачки (@) и точки (.). Напишите программу, проверяющую корректность email адреса.

Формат входных данных
На вход программе подаётся одна строка: email адрес.

Формат выходных данных
Программа должна вывести строку «YES», если email адрес является корректным, или «NO» в противном случае.

Примечание. Для настоящих email адресов недостаточно наличия символов @ и ., однако их отсутствие гарантировано влечёт за собой неверный email.
"""

email = input()

if '@' in email and '.' in email:
    print('YES')
else:
    print('NO')