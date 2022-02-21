import csv
import pandas as pd
import datetime
import random


warehouse = pd.read_csv('warehouse.csv', delimiter=',')
tg = pd.read_csv('ordered_products.csv', delimiter=',')
all_items = pd.read_csv('all_items.csv', delimiter=',')
discounts = pd.read_csv('discounts.csv', delimiter=',')
tg.index += 1
warehouse.index += 1
all_items.index += 1


def back():
    q = input('Хотите вернуться в меню?\n'
              'Нажмите любую кнопку чтобы вернуться в меню, (0) чтобы выйти')
    if q != '0':
        worker()
    elif q == '0':
        return


def delete():
    print(tg)
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
    print('Заказ был удален!')


def question():

    product = input('Введите название продукта\n')
    name = input('Введите модель\n')
    model = input('Введитье продукт\n')
    count = input('Введите кол-во\n')
    number = '0123456789'
    length = 6
    serial_number = ''.join(random.sample(number, length))
    date = datetime.date.today()
    abc = [product, name, model, count, serial_number, date]
    with open('ordered_products.csv', 'a') as fi:
        writer = csv.writer(fi)
        writer.writerow(abc)


print('''Приветствую дорогой, Работник!''')


def worker():

    choice = input('''Пожалуйста наберите номер меню для работы с программой, если закончили, то наберите 8:
1) Показать весь список товаров доступные в магазине
2) Искать товар:
3) Показать отчет
4) Выполнить заказ: 
5) Посмотреть список заказанных товаров 
6) Показать отсутствующие на складе товара
7) Показать все товары на, которых дейтсвует скидка 
8) Удалить заказ:
9) Показать удаленные товары
10) Выход\n''')

    if choice == '1':
        print(all_items[['Name', 'Model', 'Products', 'Serial number']])
        back()

    elif choice == '2':
        print(all_items[['Name', 'Model', 'Products', 'Serial number']])
        ch = input('Выберите способ поиска товаров:------>s/n\n')
        if ch == 's':
            g = int(input('Введите имя продукта:'))
            d = all_items['Serial number'].isin([g])
            print(all_items[d])
            back()

        elif ch == 'n':
            g = input('Введите имя продукта:')
            d = all_items['Name'].isin([g])
            print(all_items[d])
            back()

    elif choice == '3':
        print(all_items)
        back()

    elif choice == '4':
        question()
        back()

    elif choice == '5':
        a = pd.read_csv('ordered_products.csv', delimiter=',')
        print(a)
        back()

    elif choice == '6':
        a = warehouse['Count'] == 0
        b = warehouse.isin([a])
        print(warehouse[b])
        back()

    elif choice == '7':
        print(discounts)
        back()

    elif choice == '8':
        delete()
        worker()

    elif choice == '9':
        df1 = pd.read_csv('deleted_files.csv', delimiter=',')
        df1.index += 1
        print(df1)
        back()

    elif choice == '10':
        return
    else:
        print('Try again')
        worker()


worker()
