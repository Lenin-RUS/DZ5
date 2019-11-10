# В моих функциях кривой return или его нет вовсе
# from account_usage import play_account_use
# from main_menu import main_menu
# from victory import play_game

import Leonids_funcs

def test_author_info():
    assert Leonids_funcs.author_info() == 'Leonid Orlov'

def test_separator():
    assert Leonids_funcs.separator(5)=="*****"

def test_is_correct_choice():
    menu_items=('Пункт_1', 'Пункт_2','Пункт_3','Пункт_4','Пункт_5','Пункт_6','Пункт_7',)
    assert Leonids_funcs.is_correct_choice('5', menu_items)==True

#Грязная функция

def test_filenames():
    assert Leonids_funcs.filenames() == ['.gitignore', '123.txt', 'account_usage.py', 'file_console_manager.py', 'Leonids_funcs.py', 'LICENSE', 'main_menu.py', 'task.txt', 'test.py', 'test_filemanager.py', 'test_python.py', 'victory.py']

import account_usage

def test_get_acc_data():
    with open('acc_data.txt', 'r') as f:
        bank_summ=float(f.read())
    assert account_usage.get_acc_data() == bank_summ