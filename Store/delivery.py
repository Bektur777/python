import pandas as pd

tg = pd.read_csv('delivered_products.csv', delimiter=',')
tg.index += 1


def back():
    q = input('Хотите вернуться в меню?\n'
              'Нажмите любую кнопку чтобы вернуться в меню, (0) чтобы выйти')
    if q != '0':
        delivery()
    elif q == '0':
        return


print('Приветствую дорогой, Доставщик!')


def delivery():

    choose = input('''
Please dial the menu number to work with the program, if you have finished, then dial 7:

1.	Show the list of items for delivery 
2.	Show Delivered Goods 
3.	Deliver:
4.	Show the number of delivered items: 
5.	Show the number of ordered items: 
6.	Show my earnings 
7.	Output\n''')

    if choose == '1':
        df = pd.read_csv('ordered_products.csv', delimiter=',')
        df.index += 1
        print(df)
        back()

    elif choose == '2':
        check = pd.read_csv('delivered_products.csv', delimiter=',')
        check.index += 1
        print(check)
        back()

    elif choose == '3':
        print('Hello, these are the ordered items')
        df = pd.read_csv('ordered_products.csv', delimiter=',')
        df.index += 1
        print(df)
        ordered = input('Enter the serial number of the delivered product:')
        with open('delivered_products.csv', 'a') as f:
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

        check = pd.read_csv('delivered_products.csv', delimiter=',')
        check.index += 1
        print('Доставленные товары')
        print(check)
        back()

    elif choose == '4':
        check = pd.read_csv('delivered_products.csv', delimiter=',')
        print('Total items delivered:', len(check.index))
        back()

    elif choose == '5':
        df = pd.read_csv('ordered_products.csv', delimiter=',')
        print('Total items ordered:', len(df.index))
        back()

    elif choose == '6':
        df = pd.read_csv('delivered_products.csv', delimiter=',')
        print('Delivery costs. 550 kgs')
        print('Your salary is:', len(df.index)*550, 'kgs')
        back()

    elif choose == '7':
        return
    else:
        print('Try again')
        delivery()


delivery()
