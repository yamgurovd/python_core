"""
Цикл while подразумевает под собой немного другой подход к ограничению количества шагов, которые должны выполняться.
Он выполняется до тех пор, пока истинно его условие. Как только оно становится ложным, цикл прерывается.
Для компьютера это выглядит как: «Делай, пока не наступит ...» .

while условие:
    # Начало блока кода с телом цикла
    # пока условие истинно, цикл выполняется
    ...
    ...
    ...
    # Конец блока кода с телом цикла
# Код который будет выполняться после цикла
"""

"""
Такой цикл ещё называют циклом с предусловием. Давайте разбирать работу цикла while на примере.
Пример 2.

Условие задачи: написать цикл, который будет складывать натуральные числа, пока их сумма не превысит 500.

Заранее мы не знаем число шагов нашего цикла, но знаем условие, при котором нужно остановиться. 
Поэтому выберем цикл while и заведём две переменные для суммы и для текущего числа.
"""

S = 0  # заводим переменную-счётчик, в которой мы будем считать сумму
n = 1  # текущее натуральное число

# заводим цикл while, который будет работать пока сумма не превысит 500
while S < 500:  # делай пока ...
    S += n  # увеличиваем сумму, равносильно S = S + n
    n += 1  # так как сумма ещё не достигла нужного значения, то увеличиваем переменную-счётчик
    print("Ещё считаю ...")

print("Сумма равна: ", S)
print("Количество чисел: ", n - 1)

"""
Работая с циклом while, нужно быть внимательным, ведь если условие остановки будет всегда True, 
то цикл никогда не остановится. Бывают задачи, в которых это полезно, например, вы создадите программу, 
которая будет бесконечно обновлять и отображать время. Но часто бесконечный цикл — это ошибка начинающего программиста, 
который забыл добавить изменение условия цикла.
"""

# плохо
n = 1
while n < 10:  # в данной программе это условие всегда True, цикл будет бесконечным
    print("Hello World")

"""Чтобы остановить выполнение такого скрипта в терминале нужно нажать Ctrl+C.

Как уже обсуждалось, бывают моменты, когда необходимо специально запустить бесконечный цикл, но вопрос, как его потом 
оставить, не отключая весь скрипт? Для этого есть ключевое слово break, которое говорит, 
что цикл нужно принудительно прервать."""

# хорошо
n = 1
while True:  # в данной программе это условие всегда True, цикл будет бесконечным
    print("Hello World")
    n += 1
    if n > 10:  # условие, при достижении которого цикл while будет принудительно завершён
        break

"""Особенность использования такого цикла while с условием внутри заключается в том, 
что тело цикла точно выполнится один раз, в отличие от цикла с предусловием. Такой цикл ещё называют цикл с постусловием.

Подробнее работу с break и ещё одной командой continue разберём в следующем юните с практическими примерами."""

