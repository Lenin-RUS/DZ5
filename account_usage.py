account = 0.0
purchases = {}

def play_account_use():

    from IPython.display import clear_output
    clear_output()

    def action(num_of_action):
        global account
        global purchases

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
                purchases[buy_target] = purchases.setdefault(buy_target, 0) + spend

        if num_of_action == 3:
            for k, v in purchases.items():
                print(f'на покупку {k} потратили {v} миллиародов долларов Зимбабве.')


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