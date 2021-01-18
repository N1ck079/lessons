import os
def ch_dir():
    try:
        os.chdir(os.path.join(os.getcwd(), input('\nВведите имя папки: ')))
    except FileNotFoundError:
        print('\nНевозможно перейти\n')
    else:
        print('\nУспешно перешел.\n')
 
 
def list_dir():
    if os.listdir(os.getcwd()) != []:
        print('\nТекущая директория содержит:')
        for i in os.listdir(os.getcwd()):
            print(i)
        print()
    else:
        print('\nТекущая директория пуста.\n')
 
 
def rem_dir():
    try:
        os.rmdir(os.path.join(os.getcwd(), input('\nВведите имя папки: ')))
 
    except FileNotFoundError:
        print('\nНевозможно удалить папку которой не существует.\n')
 
    else:
        print('\nПапка успешно удалена\n')
 
 
def mk_dir():
    try:
        os.mkdir(os.path.join(os.getcwd(), input('\nВведите имя папки: ')))
    except FileExistsError:
        print('\nПапка уже существует.\n')
    else:
        print('\nПапка успешно создана\n')
 
 
def level_up():
    os.chdir(os.path.split(os.getcwd())[0])
    print('Перешел на один уровень вверх.\n')