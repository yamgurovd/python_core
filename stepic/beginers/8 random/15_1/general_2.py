"""Функция shuffle()
Функция shuffle() принимает список в качестве обязательного аргумента и перемешивает его случайным образом.

Следующий код перемешивает список numbers случайным образом, а затем выводит его содержимое:"""
import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(numbers)
print(numbers)

"""Результатом работы такого кода может быть: [4, 7, 8, 1, 2, 3, 6, 5]"""

"""Функция choice()
Функция choice() принимает список (строку) в качестве обязательного аргумента и возвращает один случайный элемент 
из переданного списка (строки).

Следующий код выводит по одному случайному элементу из строки 'BEEGEEK' и списков [1, 2, 3, 4], ['a', 'b', 'c', 'd']:"""
import random

print(random.choice('BEEGEEK'))
print(random.choice([1, 2, 3, 4]))
print(random.choice(['a', 'b', 'c', 'd']))

"""Результатом работы такого кода может быть:
E
3
c"""

"""Функция sample()
Функция sample() принимает два обязательных аргумента: список (строку) и количество случайных элементов, 
а возвращает список случайных элементов в указанном количестве.

Результатом работы кода:"""
import random

numbers = [2, 5, 8, 9, 12]

print(random.sample(numbers, 1))
print(random.sample(numbers, 2))
print(random.sample(numbers, 3))
print(random.sample(numbers, 5))

"""может быть:

[9]
[12, 5]
[9, 2, 8]
[12, 8, 9, 5, 2]"""

"""Количество случайных элементов не должно превышать длину начального списка (строки). Следующий код:"""
"""import random
 
numbers = [2, 5, 8, 9, 12]

print(random.sample(numbers, 6))
приведет к ошибке:

ValueError: Sample larger than population or is negative"""