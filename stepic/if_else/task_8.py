"""
Напишите программу, которая по введённому возрасту пользователя сообщает, к какой возрастной группе он относится:
до 13 (включительно) – детство;
от 14 до 24 (включительно) – молодость;
от 25 до 59 (включительно) – зрелость;
от 60 (включительно) – старость.

link - https://stepik.org/lesson/265081/step/12?unit=246029
"""

age = int(input("Введите возраст: "))

if age <= 13:
    print("детсво")
elif 14 <= age <= 24:
    print("Молодость")
elif 25 <= age <= 59:
    print("зрелость")
else:
    print("старость")