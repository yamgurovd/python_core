"""Количество цифр
На вход программе подается строка текста. Напишите программу, которая подсчитывает количество цифр в данной строке.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести количество цифр в данной строке."""

text = input()
counter = 0

for i in text:
    if "0" <= i <= "9":
        counter += 1

print(counter)

# Второй способ решения
s = input()
cnt = 0
for i in s:
    if i.isdigit() == True:
        cnt += 1
print(cnt)