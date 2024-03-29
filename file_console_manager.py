import main_menu
import os
import shutil
import platform
import victory
import account_usage

account = 0.0
purchases = {}

run_again=True
while run_again==True:
    my_choice = main_menu.main_menu()

    # после выбора пользователь вводит название папки, создаем её в рабочей директории
    if my_choice==1:
        new_dir_name=input('Введите имя новой папки: ')
        os.mkdir(new_dir_name) if not os.path.exists(new_dir_name) else print('такая папка уже есть!')    # <----------------------------------1 Тернарный оператор
    #после выбора пользователь вводит название папки или файла, удаляем из рабочей директории если такой есть
    if my_choice==2:
        file_or_dir_to_del=input('Введите имя папки или файла для удаления: ')
        os.rmdir(file_or_dir_to_del)

    #после выбора пользователь вводит название папки/файла и новое название папки/файла. Копируем
    if my_choice==3:
        file_to_copy=input('Введите имя папки или файла для копирования: ')
        file_new_name=input('Введите новое имя папки или файла: ')
        shutil.copy(file_to_copy,file_new_name)

    # вывод всех объектов в рабочей папке
    if my_choice==4: print(os.listdir())

    #вывод только папок которые находятся в рабочей папке
    if my_choice==5:
        onlydirs = [f for f in os.listdir() if os.path.isdir(f)]    # <----------------------------------2 (Это уже давно написал)
        print(onlydirs)

    #вывод только файлов которые находятся в рабочей папке
    if my_choice==6:
        onlyfiles = [f for f in os.listdir() if os.path.isfile(f)]    # <----------------------------------3 (Это уже тоже давно написал)
        print(onlyfiles)

    #вывести информацию об операционной системе (можно использовать пример из 1-го урока)
    if (my_choice==7): print(platform.uname())

    #вывод информации о создателе программы
    if my_choice==8: print(os.getlogin())

    #запуск игры викторина из предыдущего дз
    if my_choice==9: victory.play_game()

    #запуск программы для работы с банковским счетом из предыдущего дз (задание учебное, после выхода из программы управлением счетом в главной программе сумму и историю покупок можно не запоминать)
    if my_choice==10: account_usage.play_account_use()

    #усложненное задание пользователь вводит полный /home/user/... или относительный user/my/... путь. Меняем рабочую директорию на ту что ввели и работаем уже в ней
    if my_choice==11:
        print('Текущая рабочая папка: ', os.getcwd())
        new_dir_path=input('Введите новый путь рабочей папки: ')
        if os.path.exists(new_dir_path):
            os.chdir(new_dir_path)
            print('Текущая рабочая папка: ', os.getcwd())
        elif os.path.exists(os.path.join(os.getcwd(), new_dir_path)):
            os.chdir(os.path.join(os.getcwd(), new_dir_path))
            print('Текущая рабочая папка: ', os.getcwd())
        else:
            print('Заданной папки нет')  # Можно дальше создать ее, или искать на диске, но это уже другая история ))

    if my_choice==12: run_again=False

    if my_choice==13:
        with open('listdir.txt', 'w') as f:
            onlydirs = [f for f in os.listdir() if os.path.isdir(f)]
            onlyfiles = [f for f in os.listdir() if os.path.isfile(f)]
            f.write(f'files:{onlyfiles} \n')
            f.write(f'dirs:{onlydirs}')
