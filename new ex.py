# Первое задание
same_word = int(input('Введите число, которое делится на 1000 без остатка :'))
if same_word % 1000 == 0:
    print('millennium')
else:
    print('не правильное число')

# Второе задание
guests = int(input('Введите кол-во гостей: '))
if guests > 50:
    print('Заказать ресторан')
elif guests > 20:
    print('Идти в кофе')
elif guests < 20:
    print('Отпразднуем дома')

# Третье задание
my_str = input('Введите слово :')
x = len(my_str)
if x > 10:
    print(my_str, '!!!')
else:
    print(my_str[2])

# Четвертое задание
my_str = input('Введите слово:')
one = my_str[0]
second = my_str[-1]
x = len(my_str)
long = x / 2
if x % 2 == 0:
    print(my_str[int(long) - 1:int(long)])
elif x % 2 != 0:
    print(my_str[int(long)])
if one == second:
    print(my_str[1:-1])
else:
    print('Совпадений нет')
