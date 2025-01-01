"""Ходы коня 🐎
На шахматной доске 8×8 стоит конь. Напишите программу, которая отмечает положение коня на доске и все клетки,
которые бьет конь. Клетку, где стоит конь, отметьте английской буквой N, а клетки, которые бьет конь,
отметьте символами *, остальные клетки заполните точками.

Формат входных данных
На вход программе подаются координаты коня на шахматной доске в шахматной нотации (то есть в виде e4,
где сначала записывается номер столбца (буква от a до h, слева направо), затем номеру строки (цифра от 1 до 8, снизу вверх)).

Формат выходных данных
Программа должна вывести на экран изображение доски, разделяя элементы пробелами.

Примечание. Шахматная доска имеет вид:"""

# Ввод координат коня
knight_position = input("Введите координаты коня (например, e4): ")

# Преобразование шахматной нотации в индексы
column = ord(knight_position[0]) - ord('a')  # Преобразуем 'a'-'h' в 0-7
row = int(knight_position[1]) - 1  # Преобразуем '1'-'8' в 0-7

# Возможные ходы коня
moves = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]

# Инициализация шахматной доски
board = [['.' for _ in range(8)] for _ in range(8)]

# Установка позиции коня
board[row][column] = 'N'

# Установка клеток, которые бьет конь
for move in moves:
    new_row = row + move[0]
    new_column = column + move[1]
    if 0 <= new_row < 8 and 0 <= new_column < 8:
        board[new_row][new_column] = '*'

# Вывод доски
for row in board:
    print(' '.join(row))