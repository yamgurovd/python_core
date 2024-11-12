"""Тема урока: вложенные циклы
Вложенные циклы
Операторы break и continue во вложенных циклах
Решение задач
Аннотация. Вложенные, находящиеся внутри других циклов, циклы.

Вложенные циклы
Вложенный цикл расположен в еще одном цикле. Часы служат хорошим примером работы вложенного цикла. Секундная, минутная и
часовая стрелки вращаются вокруг циферблата.Часовая стрелка смещается всего на 1 шаг для каждых 60 шагов минутной стрелки.
И секундная стрелка должна сделать 60 шагов для 1 шага минутной стрелки. Это означает, что для каждого полного оборота
часовой стрелки (12 шагов), минутная стрелка делает 720 шагов."""

"""Рассмотрим цикл, который частично моделирует электронные часы. Он показывает секунды от 0 до 59:"""
for seconds in range(60):
    print(seconds)

"""Можно добавить переменную minutes и вложить цикл написанный выше внутрь еще одного цикла, который повторяется 60 раз:"""
for minutes in range(60):
    for seconds in range(60):
        print(minutes, ':', seconds)

"""Для того, чтобы сделать модель законченной, можно добавить еще одну переменную для подсчета часов:"""
for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hours, ':', minutes, ':', seconds)

"""Самый внутренний цикл сделает 60 итераций для каждой итерации среднего цикла. Средний цикл сделает 60 итераций 
для каждой итерации самого внешнего цикла. Когда самый внешний цикл сделает 24 итерации, средний сделает 24⋅60=1440 итераций, 
и самый внутренний цикл сделает 24 ⋅60⋅60=86400 24 ⋅60⋅60=86400 итераций!

Пример имитационной модели часов подводит нас к нескольким моментам, имеющим отношение к вложенным циклам:

вложенный цикл выполняет все свои итерации для каждой отдельной итерации внешнего цикла;
вложенные циклы завершают свои итерации быстрее, чем внешние циклы;
для того, чтобы получить общее количество итераций вложенного цикла, надо перемножить количество итераций всех циклов.
"""

"""Операторы break и continue во вложенных циклах
Оператор break выполняет прерывание ближайшего цикла в котором он расположен. Аналогично, оператор continue осуществляет 
переход на следующую итерацию ближайшего цикла."""
for i in range(3):
    for j in range(3):
        print(i, j)

"""Изменим код, добавив во вложенный цикл условный оператор с оператором break:"""
for i in range(3):
    for j in range(3):
        if i == j:
            break
        print(i, j)

"""Изменим оператор прерывания break на оператор continue:"""

for i in range(3):
    for j in range(3):
        if i == j:
            continue
        print(i, j)


"""Для того чтобы завершить весь вывод таблицы звездочек, нам нужно выполнить этот цикл восемь раз. 
Мы можем поместить этот цикл в еще один цикл, который делает восемь итераций, как показано ниже:"""

for i in range(8):
    for j in range(6):
        print('*', end='')
    print()

"""Внешний цикл делает восемь итераций. Во время каждой итерации этого цикла внутренний цикл делает 6 итераций. 
(Обратите внимание, что в строке 4 после того, как все строки были напечатаны, мы вызываем функцию print(). 
Мы должны это сделать, чтобы в конце каждой строки продвинуть экранный курсор на следующую строку. 
Без этой инструкции все звездочки будут напечатаны на экране в виде одной длинной строки.)

Давайте рассмотрим еще один пример. Предположим, что вы хотите напечатать звездочки в комбинации, которая похожа 
на приведенный ниже звездный треугольник:"""


"""Представим эту комбинацию звездочек, как сочетание строк и столбцов. В этой комбинации всего восемь строк. 
В первой строке один столбец. Во второй строке – два столбца. В третьей строке – три. И так продолжается до восьмой строки, 
в которой восемь столбцов."""
for i in range(8):
    for j in range(i + 1):
        print('*', end='')
    print()