acc_data_file = 'acc_data.txt'
orders_data_file='order_data.txt'
import os

def get_acc_data():
    if not acc_data_file in os.listdir():
        f=open(acc_data_file, 'x')
        f.write('0')
        f.close
    with open(acc_data_file, 'r') as f:
        account=f.read()
    return float(account)

def ch_acc_data(acc_sum):
    with open(acc_data_file, 'w') as f:
        f.write(str(acc_sum))

def add_order(spend, buy_target):
    if not orders_data_file in os.listdir():
        f=open(orders_data_file, 'x', encoding='utf8')
        f.close
    with open(orders_data_file, 'a', encoding='utf8') as f:
            f.write(f'{buy_target},{spend} \n')

def all_orders():
    with open(orders_data_file, 'r', encoding='utf8') as f:
        for line in f:
            z=line.split(',')
            print(f'Покупка: {z[0]}, на сумму: {z[1]}', end='')




def play_account_use():

    def action(num_of_action):
        account =  get_acc_data()  # Прочитали начальное состояние счета
        if num_of_action == 1:
            acc_add = float(input(f'Введите сумму пополнения счета: '))
            account +=  acc_add

        if num_of_action == 2:
            spend = float(input(f'Введите сумму покупки: '))
            if spend > account:
                print('Денег не хватает')
            else:
                buy_target = input(f'Введите название товара: ')
                account -= spend
                add_order(spend, buy_target)

        if num_of_action == 3:
            all_orders()


        ch_acc_data(account)  # Занесли состояние счет после операции


    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = int(input('Выберите пункт меню по работе с банковским счетом: '))

        if choice in range(4):
            action(choice)

        elif choice == 4:
            print('Выход')
            break

        else:
            print('Неверный пункт меню')