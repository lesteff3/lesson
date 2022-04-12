# Нахождение факториала до 'n' включительно
# fact = int(input('Введите число: '))
#
#
# def factorial(fact):
#     pr = 1
#     for i in range(2, fact + 1):
#         pr = pr * i
#     print(f'Факториал числа {fact} = {pr}')
#
#
# factorial(fact)


# Задание 7.07



# def send_name(*name):
#     for names in name:
#         print(f'Hello {names}')
#
#
# send_name("Максим", "Юра", "Вася", "Светлана", "Полина")




# вывод четных ключей списка имен


#
# def name_person(*name):
#     for names in name:
#         my_names = len(names)
#         if my_names % 2 == 0:
#             print(f'Hello {names} {my_names}')
#         else:
#             print('Это имя нечетное!!!')
#
#
# name_person("Максим", "Юра", "Вася", "Светлана", "Полина")
#




# Задание 7.06

# def my_sum(*numbers):
#     a = max(numbers)
#     print(f'Максимальное значение списка {a}')
#     b = sum(numbers)
#     print(f'Сумма списка аргументов = {b}')
#
#
# my_sum(55, 66, 80, 99, 32)