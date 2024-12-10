"""Очень странные дела 📻
Джим Хоппер с помощью радиоприемника пытается получить сообщение Оди. На приёмник ему поступает
n
n различных последовательностей кода Морзе. Декодировав их, он получает последовательности из цифр и букв строчного
латинского алфавита. При этом только в сообщениях Оди содержится число
11, причём минимум 3 раза. Помогите определить Джиму количество сообщений от Оди.

Формат входных данных
В первой строке подаётся число n – количество сообщений, в последующих n строках вводятся сами сообщения.

Формат выходных данных
Программа должна вывести количество сообщений от Оди.

Примечание. Обратите внимание, что в сообщениях Оди вхождения числа 11 должны быть непересекающимися.
Другими словами, если мы нашли вхождение числа 11,
то следующее вхождение должно начинаться строго после окончания предыдущего. Например, в строке '111'
содержится одна такая последовательность, в то время как в '1111' их уже две."""

number = int(input())
count = 0
for i in range(number):
    temp=input()
    if temp.count('11') >= 3:
        count += 1
print(count)