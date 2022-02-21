import csv
import pandas as pd

pd.read_csv('accounts.csv', delimiter=',')


def account():

    pd.read_csv('accounts.csv', delimiter=',')
    acc = input('Enter your account, please!\ndirector/worker/delivery------>').lower()
    if acc == 'director' or acc == 'worker' or acc == 'delivery':
        fail = 3
        while True:
            log = input('login:')
            pas = input('password:')
            with open("accounts.csv") as File:
                reader = csv.DictReader(File)
                check = []
                for row in reader:
                    check.append(row)
                for info in check:
                    if info.get("Name") == acc and info.get("Login") == log and info.get("Password") == pas:
                        log = True

            if log == True:

                if acc == 'director':
                    import main
                    return

                elif acc == 'worker':
                    import worker
                    return

                elif acc == 'delivery':
                    import delivery
                    return
            else:
                if fail == 0:
                    print('Please, try the next time!')
                    break
                elif fail >= 0:
                    print('Wrong password or login.\nYou have', fail, 'attempts left')
                    fail -= 1
    else:
        print('Sorry, there is no such account. Try again, please')
        account()


def registration():

    name = input('Choose an account worker/delivery\n').lower()
    while name == 'delivery' or name == 'worker':
        login = input('Enter your loging:')
        password = input('Enter your password:')
        password_1 = input('Enter your password, again:')
        if password == password_1:
            common = [name, login, password]
            with open('accounts.csv', 'a+') as f:
                writer = csv.writer(f)
                writer.writerow(common)
            pd.read_csv('accounts.csv', delimiter=',')
            account()
        else:
            print('Try again')
            continue
    else:
        print('Try again')
        registration()


def entrance():

    entrances = input('''Welcome to The Cellular Accessories Store
Do you have an account?---------->yes/no\n''').lower()

    if entrances == 'no':
        registration()
    elif entrances == 'yes':
        account()
    else:
        print('Try again')
        return entrance()


entrance()
