# summa = 0
# while True:
#     a = input('введите число :')
#     if a == 'stop':
#         print("общая сумма введенных чисел = ", summa)
#         break
#     else:
#         r = int(a)
#         summa += r
#     print('Сумма = ', summa)

my_list = [10, 5, 6, 8, 16, 23]
sum = 0
for j in my_list:
    if j >= 10:
        sum += j
print('Cумма чисел больше 10 в списке =', sum)

# n = int(input('Введите целое число :'))
# a = 1
# s = 0
# while a <= n:
#     s = a + s
#     a = a + 1
#     v = s*s*s
#     print(f'Сумма кубов всех целых чисел от 1 до {n} = {v}')
#








# from random import randint
# while True:
#     a = randint(1, 10)
#     print(a)
#     if a == 7:
#         print('Выпало число 7')
#         break
