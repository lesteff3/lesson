def inch(centi):
    print(f'В {centi} дюймах {centi * 2.54} сантиметров')


inch(2)


def centimeter(inches):
    print(f'В {inches} сантиметрах {inches / 2.54} дюймов')


centimeter(2)


def miles(km):
    print(f'В {km} милях {km * 1.6} киллометров')


miles(2)


def kilomiters(mil):
    print(f'В {mil} километрах {mil / 1.6} миль')


kilomiters(3)


def pounds(killogramm):
    print(f'в {killogramm} фунтах {killogramm / 2.205} килограмм')


pounds(4)


def kilo(pound):
    print(f'в {pound} килограммах {pound * 2.205} фунтов')


kilo(6)


def ounces(gramm):
    print(f'в {gramm} унциях {gramm * 28.35} грамм')


ounces(4)


def grams(ounc):
    print(f'в {ounc} граммах {ounc / 28.35} унции')


grams(7)


def gallon(litrs):
    print(f'В {litrs} галлонах {litrs * 3.785} литров')


gallon(9)


def litr(gallons):
    print(f'В {gallons} литрах {gallons / 3.785} галлонов')


litr(10)


def pint(litre):
    print(f'В {litre} пинтах {litre / 2.113} литров')


pint(2)


def litraj(pints):
    print(f'В {pints} литрах {pints * 2.113} пинта')


litraj(3)


def number_translation():
    while True:
        my_list = '1.Дюймы в сантиметры\n' \
                  '2. Сантиметры в дюймы\n' \
                  '3. Мили в километры\n' \
                  '4. Километры в мили\n' \
                  '5. Фунты в килограммы\n' \
                  '6. Килограммы в фунты\n' \
                  '7. Унции в граммы\n' \
                  '8. Граммы в унции\n' \
                  '9. Галлон в литры\n' \
                  '10. Литры в галлоны\n' \
                  '11. Пинты в литры\n' \
                  '12. Литры в пинты\n'
        print(my_list)
        my_selection = int(input('Выберите вариант от 1 до 12 :'))
        if my_selection == 0:
            print('Вы вышли из цикла')
            break
        elif my_selection == 1:
            inch(int(input('Введите кол-во дюймов: ')))
        elif my_selection == 2:
            centimeter(int(input('Введите кол-во сантиметров :')))
        elif my_selection == 3:
            miles(int(input('Введите кол-во миль :')))
        elif my_selection == 4:
            kilomiters(int(input('Введите кол-во киллометров : ')))
        elif my_selection == 5:
            pounds(int(input('Введите кол-во фунтов : ')))
        elif my_selection == 6:
            kilo(int(input('Введите кол-во килограмм : ')))
        elif my_selection == 7:
            ounces(int(input('Введите кол-во унций : ')))
        elif my_selection == 8:
            grams(int(input('Введите кол-во грамм : ')))
        elif my_selection == 9:
            gallon(int(input('Введите кол-во галлон : ')))
        elif my_selection == 10:
            litr(int(input('Введите кол-во литров : ')))
        elif my_selection == 11:
            pint(int(input('Введите кол-во пинтов : ')))
        elif my_selection == 12:
            litraj(int(input('Введите кол-во литров : ')))
        else:
            print("Введите нужное число из списка")


number_translation()
