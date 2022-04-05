# Первая задача
my_list = [10, 20, 3, 6, 9, 16, 22, 200]
n = -2
v = 0
for j in my_list:
    if j >= 0:
        print(j * -2, end='')


# Вторая задача
my_list = [10, 20, 3, 6, 9, 16, 22, 200]
n = 0
sum = 0
for j in my_list:
    if j % 2 == 0:
        n = + 1
        sum += n
print(f'Всего элементов кратных двум {sum} ', end='')

# Третья задача

my_ex = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
for key in list(my_ex.keys()):
    my_ex[key + str(len(key))] = my_ex.pop(key)
print(my_ex)

# Четвертая задача
my_list = [1, 2, 3, 4, 5]
for j in my_list:
    v = my_list[1::] + my_list[:1]
print(v)

# Пятая задача

fib1 = 1
fib2 = 1
n = int(input('введите число'))
print(fib1, fib2, end=' ')
while n > 2:
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')
    n -= 1