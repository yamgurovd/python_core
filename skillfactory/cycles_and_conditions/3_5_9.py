"""
Дано натуральное восьмизначное число. Выясните, является ли оно палиндромом
(читается одинаково слева направо и справа налево).
"""

dig = 1234321
convert_dig = str(dig)

# print(convert_dig)

dig_ch = convert_dig[::-1]

if convert_dig == dig_ch:
    print("Число является палиндромом")