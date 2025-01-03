"""Сортировка простыми вставками
Алгоритм сортировки простыми вставками делит список на 2 части — отсортированную и неотсортированную.
Из неотсортированной части извлекается очередной элемент и вставляется на нужную позицию в отсортированной части,
в результате чего отсортированная часть списка увеличивается, а неотсортированная уменьшается. Так происходит,
пока не исчерпан набор входных данных  и не отсортированы все элементы.

Сортировка простыми вставками наиболее эффективна, когда список уже частично отсортирован и элементов массива немного.
Если элементов в списке меньше 10, то этот алгоритм — один из самых быстрых."""

"""Рассмотрим его работу на примере сортировки списка a = [5, 1, 8, 2, 4] по возрастанию.

Первый проход:

Делим список на две части: отсортированную [5] и неотсортированную [1, 8, 2, 4].

Извлекаем первый элемент 1 из неотсортированной части списка и находим ему место в отсортированной части:

[1, 5, 8, 2, 4].

Второй проход:

Делим список на две части: отсортированную [1, 5] и неотсортированную [8, 2, 4].

Извлекаем первый элемент 8 из неотсортированной части списка и находим ему место в отсортированной части:

[1, 5, 8, 2, 4].

Третий проход:

Делим список на две части: отсортированную [1, 5, 8] и неотсортированную [2, 4].

Извлекаем первый элемент 2 из неотсортированной части списка и находим ему место в отсортированной части:

[1, 2, 5, 8, 4].

Четвертый проход:

Делим список на две части: отсортированную [1, 2, 5, 8] и неотсортированную [4].

Извлекаем первый элемент 4 из неотсортированной части списка и находим ему место в отсортированной части:

[1, 2, 4, 5, 8].

Теперь список отсортирован, и алгоритм может быть завершен."""

"""Реализация алгоритма
Пусть требуется отсортировать по возрастанию список чисел: a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99].

Следующий программный код реализует алгоритм сортировки простыми вставками:"""
a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6, 8, -2, 99]
n = len(a)

for i in range(1, n):
    elem = a[i]  # берем первый элемент из неотсортированной части списка
    j = i

    # пока элемент слева существует и больше нашего текущего элемента
    while j >= 1 and a[j - 1] > elem:
        # смещаем j-й элемент отсортированной части вправо
        a[j] = a[j - 1]
        # сами идём влево, дальше ищем место для нашего текущего элемента
        j -= 1

    # нашли место для нащего текущего элемента из неотсортированной части
    # и вставляем его на индекс j в отсортированной части
    a[j] = elem

print('Отсортированный список:', a)
"""Результатом выполнения такого кода будет:

Отсортированный список: [-67, -3, -2, 0, 1, 6, 7, 8, 9, 12, 34, 45, 99, 1000]"""
