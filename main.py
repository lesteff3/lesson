# #  Первое задание
first = int(input('Введите первое целое число: '))
second = int(input('Введите второе целое число: '))
print("Сумма:", first + second)
print("Разность:", first - second)
print("Произведение", first * second)

# #  Второе задание
one = int(input("Введите первое целое число: "))
two = int(input("Введите второе целое число: "))
if (one < 0):
    print("Число отрицательное")
elif (two < 0):
    print("Число отрицательное")
else:
    print(f"Среднее арифмитическое: {(one + two) / 2}\nСреднее геометрическое: {(one + two) ** 0.5}")

# #  Третье задание

import math

a = int(input('Введите 1 катет прямоугольника: '))
b = int(input('Введите 2 катет прямоугольника: '))
print('Гепотенуза прямоугольника равна:', math.sqrt(a ** 2 + b ** 2))
print('Площадь прямоульника равна:', 0.5 * a * b)

## Четвертое задание

long = int(input('введите длину ребра: '))
print("объем равен :" + str(long ** 3))
print("площадь боковой поверхности равна :" + str(long * long * 4))
