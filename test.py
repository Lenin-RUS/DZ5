
import platform
import sys
import os


print('Текущая рабочая папка: ', os.getcwd())
new_dir_path=input('Введите новый путь рабочей папки: ')
print(new_dir_path)
print(os.path.exists(new_dir_path))
print(os.path.join(os.getcwd(), new_dir_path))
print(os.path.exists(os.path.join(os.getcwd(), new_dir_path)))
if os.path.exists(new_dir_path):
    os.chdir(new_dir_path)
    print('Текущая рабочая папка: ', os.getcwd())
elif os.path.exists(os.path.join(os.getcwd(), new_dir_path)):
    os.chdir(os.path.join(os.getcwd(), new_dir_path))
    print('Текущая рабочая папка: ', os.getcwd())
else:
    print('Заданной папки нет')  # Можно дальше создать ее, но это уже другая история ))