
# 01 Задание
def numbers(my_list):
    new_list = []
    count = 0
    for i in my_list:
        if i not in new_list:
            count = count + 1
            new_list.append(i)
    print(f"Список со всеми элементами списка {my_list}")
    print(f"Уникальные значения списка {new_list}")


numbers([1, 2, 3, 6, 1, 7, 2, 4, 3, 8, 8, 8, 9])


# # 02 Задание
#
def string_test(my_str):
    upper = 0
    lower = 0
    for x in my_str:
        if x.isupper():
            upper += 1
        elif x.islower():
            lower += 1
    print(f"Введенная строка : {my_str}")
    print(f"Букв с верхним регистром : {upper}")
    print(f"Букв с нижним регистром : {lower}")


string_test("Логика может привести Вас от пункта А к пункту Б, а воображение — куда угодно.")


# 03 Задание

def check_palindrome(str_1, str_2, str_3):
    reversed_string = str_1[::-1]
    string_two = str_2[::-1]
    string_third = str_3[::-1]
    if str_1 != reversed_string:
        print(f'{str_1} слово не палиндром')
    else:
        print(f'{str_1} слово  палиндром')
    if str_2 != string_two:
        print(f'{str_2} слово не палиндром')
    else:
        print(f'{str_2} слово палиндром')
    if str_3 != string_third:
        print(f'{str_3} слово не палиндром')
    else:
        print(f'{str_3} слово палиндром')


check_palindrome('шалаш', 'максим', 'казак')


# 04 Задание
def epam(text):
    gmail = ' lesteff2016@gmail.com'
    text += gmail
    x = len(text)
    print(f'Всего символов {x}')
    count = 0
    vowels = set("aeiou")
    for letter in text:
        if letter in vowels:
            count += 1
    print(f"Количество гласных {count}")
    new_text = str.upper(text)
    for i in range(0, len(new_text), 18):
        print(i, new_text[i])


epam(
    "The Zen of Python, by Tim Peters "
    "Beautiful is better than ugly."
    "Explicit is better than implicit."
    "Simple is better than complex."
    "Complex is better than complicated. "
    "Flat is better than nested."
    "Sparse is better than dense."
    "Readability counts."
    "Special cases arent special enough to break the rules."
    "Although practicality beats purity."
    "Errors should never pass silently.Unless explicitly silenced."
    "In the face of ambiguity, refuse the temptation to guess."
    "There should be one-- and preferably only one --obvious way to do it."
    "Although that way may not be obvious at first unless you're Dutch."
    "Now is better than never."
    "Although never is often better than *right* now."
    "If the implementation is hard to explain, it's a bad idea."
    "If the implementation is easy to explain, it may be a good idea."
    "Namespaces are one honking great idea -- let's do more of those!")
