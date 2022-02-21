import pandas as pd
import csv
import datetime
import random

tgg = pd.read_csv('ordered_products.csv', delimiter=',')
all_items = pd.read_csv('all_items.csv', delimiter=',')
all_items.index += 1
tgg.index += 1


def adding_products():

    ordered = input('Enter the serial number:')
    with open('all_items.csv', 'a+') as f:
        with open('delivered_products.csv') as ff:
            reader = ff.readlines()
            for row in reader:
                print(row)
                if ordered in row:
                    f.write(row)
                    f.write('\n')

    with open("delivered_products.csv", "w") as f:
        for row in reader:
            print(row)
            if not(ordered in row):
                f.write(row)


def question():
    product = input('Введите название продукта\n')
    name = input('Введите модель\n')
    model = input('Введите продукт\n')
    count = input('Введите кол-во\n')
    number = '0123456789'
    length = 6
    serial_number = ''.join(random.sample(number, length))
    date = datetime.date.today()
    abc = [product, name, model, count, serial_number, date]
    with open('ordered_products.csv', 'a') as fi:
        writer = csv.writer(fi)
        writer.writerow(abc)


def delete():
    ordered = input('Введите серийный номер:')
    with open('deleted_files.csv', 'a+') as f:
        with open('ordered_products.csv') as ff:
            reader = ff.readlines()
            for row in reader:
                if ordered in row:
                    f.write(row)
                    f.write('\n')

    with open("ordered_products.csv", "w") as f:
        for row in reader:
            if not (ordered in row):
                f.write(row)


def search():
    ch = input('Choose how to search for products:------>s/n\n')
    if ch == 's':
        searching = int(input('Enter the serial number:\n'))
        search_s = tgg['Serial number'].isin([searching])
        print(tgg[search_s])
        menu()
    elif ch == 'n':
        g = input('Enter the product name:')
        d = tgg['Name'].isin([g])
        print(tgg[d])
        menu()


def back():
    q = input('Хотите вернуться в меню?\n'
              'Нажмите любую кнопку чтобы вернуться в меню, (0) чтобы выйти')
    if q != '0':
        director()
    elif q == '0':
        return


def back1():
    q = input('Хотите вернуться в меню?\n'
              'Нажмите любую кнопку чтобы вернуться в меню, (0) чтобы выйти')
    if q != '0':
        menu()
    elif q == '0':
        return


def back2():
    q = input('Хотите вернуться в меню?\n'
              'Нажмите любую кнопку чтобы вернуться в меню, (0) чтобы вернуться в меню админа')
    if q != '0':
        menu2()
    elif q == '0':
        menu()


def menu2():
    ordered = pd.read_csv('ordered_products.csv', delimiter=',')
    ordered.index += 1
    ask = input('''
Если вы хотите узнать больше информации, выберите от 1 до 6:
1) Просмотреть заказанные товары
2) Просмотреть первые три заказа
3) Просмотреть три последних заказа
4) Поиск заказанных товаров
5) Просмотр удаленных заказов
6) Вернуться в меню''')

    if ask == '1':
        print(ordered)
        back2()

    elif ask == '2':
        print(ordered.head(3))
        back2()

    elif ask == '3':
        print(ordered.tail(3))
        back2()

    elif ask == '4':
        search()
        menu2()

    elif ask == '5':
        df1 = pd.read_csv('deleted_files.csv', delimiter=',')
        df1.index += 1
        print(df1)
        back2()
    elif ask == '6':
        menu()


def menu():

    ask = input('''Меню специальных возможностей, здесь вы можете:
Добавлять либо удалять товары со списка, также здесь доступна информация о поставщиках и отчетах:
Пожалуйста наберите номер меню для работы с программой:

1) Просмотр доставленных товаров
2) Добавления товаров в магазин
3) Посмотреть информацию о заказанных товаров
4) Отчеты
5) Выход (в меню)''')

    if ask == '1':
        df = pd.read_csv('delivered_products.csv', delimiter=',')
        df.index += 1
        print(df)
        back1()

    elif ask == '2':
        adding_products()
        menu()
        back1()

    elif ask == '3':
        menu2()
        back1()

    elif ask == '4':
        df = pd.read_csv('ordered_products.csv', delimiter=',')
        check = pd.read_csv('delivered_products.csv', delimiter=',')
        print('Total items ordered:', len(df.index), '\nTotal items delivered:', len(check.index))
        print('The salary of the delivery man is:', len(check.index) * 550, 'kgs')
        back1()

    elif ask == '5':
        director()

    else:
        print('Please, try again')
        menu()


print('''Приветствую дорогой, Директор!
Пожалуйста наберите номер меню для работы с программой, если закончили, то наберите 6:''')


def director():

    ask = input('''
1) Show the list of all products (Shows the list of products in the store)
2) Show quantity of items (Shows the number of items per category)
3) Show most numerous items
4) Show most numerous items (Shows the least number of items in category)
5) Special Features Menu
6) Exit (from program)
Enter the number:''')
    if ask == '1':
        all_itemss = pd.read_csv('all_items.csv', delimiter=',')
        all_itemss.index += 1
        print(all_itemss[['Name', 'Model', 'Products', 'Serial number']])
        back()

    elif ask == '2':
        print(all_items[['Name', 'Model', 'Products', 'Count', 'Serial number']])
        back()

    elif ask == '3':
        print(all_items[all_items['Count'] == all_items['Count'].max()])
        back()

    elif ask == '4':
        print(all_items[all_items['Count'] == all_items['Count'].min()])
        back()

    elif ask == '5':
        menu()

    elif ask == '6':
        return

    else:
        print('Такого значение нет!')
        director()


director()
