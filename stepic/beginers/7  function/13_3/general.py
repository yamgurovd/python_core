"""Тема урока: локальные и глобальные переменные
Локальные переменные
Область видимости локальной переменной
Глобальные переменные
Глобальные константы
Решение задач
Аннотация. Локальные и глобальные переменные."""

"""Локальные переменные
Локальными называются переменные, объявленные внутри функции и доступные только ей самой. 
Программный код за пределами функции к ним доступа не имеет.

Рассмотрим функцию print_texas(), которая выводит информацию о количестве птиц, обитающих в Техасе."""


def print_texas():
    birds = 5000
    print('В Техасе обитает', birds, 'птиц.')


"""В теле функции мы создаем переменную birds, которой присваивается значение, равное 5000. 
Такая переменная является локальной для функции print_texas(). 
Всякий раз, когда переменной внутри функции присваивается значение, в результате создаётся локальная переменная. 
Она принадлежит функции, в которой создаётся, и к ней получает доступ только программный код этой функции."""

"""Термин “локальная” указывает на то, что переменная может использоваться лишь в этом месте — внутри функции, 
в которой создается.

Если программный код одной функции попытается обратиться к локальной переменной, принадлежащей другой функции, 
произойдёт ошибка.

Рассмотрим следующий программный код:"""


def print_texas():
    birds = 5000
    print('В Техасе обитает', birds, 'птиц.')


def print_california():
    print('В Калифорнии обитает', birds, 'птиц.')


"""Функция print_california() обращается к локальной переменной birds функции print_texas(). 
Вызов функции print_california(), приводит к ошибке:

NameError: name 'birds' is not defined"""

"""Локальные переменные скрыты от других функций, поэтому другие функции могут иметь собственные локальные 
переменные с тем же именем. Например,"""


def print_texas():
    birds = 5000
    print('В Техасе обитает', birds, 'птиц.')


def print_california():
    birds = 9000
    print('В Калифорнии обитает', birds, 'птиц.')


"""В каждой из этих двух функций есть локальная переменная с именем birds. Но они никогда не видны одновременно, 
так как находятся в разных функциях.

Когда выполняется функция print_texas(), видима переменная birds, значение которой равно 5000. 
Когда выполняется функция print_california(), видима переменная birds, значение которой равно 9000.

Разные функции могут иметь локальные переменные с одинаковыми именами, 
потому что они не видят локальных переменных друг друга."""

"""Область видимости переменной
Область видимости переменной – часть программы, в которой можно к ней обращаться (та функция, где она создана). 
Переменная видима программному коду только в области её видимости. Никакая инструкция за пределами функции 
не может обращаться к такой переменной.

К локальной переменной не может обращаться программный код, который появляется внутри функции до того, 
как переменная была создана.

Например, если в функции print_texas() поменять местами строки кода:"""


def print_texas():
    print('В Техасе обитает', birds, 'птиц.')
    birds = 5000


"""то при вызове этой функции получим ошибку:

UnboundLocalError: local variable 'birds' referenced before assignment
Ошибка возникла в результате преждевременного обращения к еще не объявленной локальной переменной birds."""

"""Область видимости параметрической переменной
Область видимости параметрической переменной — функция, в которой этот параметр используется. 
К параметрической переменной имеет доступ весь программный код этой функции.

Рассмотрим уже известную нам функцию:"""


def draw_box(height, width):
    for i in range(height):
        print('*' * width)


"""Параметрические переменные тут height, width. Внутри функции объявляется одна локальная переменная i.

Примечания
Примечание 1. Параметрическая переменная тоже локальная.

Примечание 2. Память для локальных переменных выделяется на время исполнения данной функции в специальной области, 
называемой стеком. При завершении работы функции память освобождается, внутренние результаты работы функции не 
сохраняются от одного обращения к другому."""
