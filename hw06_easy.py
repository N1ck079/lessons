# Задача-1:
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:

def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.

    Исключения:
        - ValueError: вычисление не возможно.
    """
    if a * b >= 0:
        return (a * b) ** 0.5
    else:
        raise ValueError("Невозможно определить среднее геометрическое "
                         "введенных чисел.")


try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = avg(a, b)
    print("Среднее геометрическое = {:.2f}".format(c))
except ValueError as err:
    print("Ошибка:", err, ". Проверьте введенные числа.")
except Exception as err:
    print("Ошибка:", err)

# ПРИМЕЧАНИЕ: Для решения задач 2-4 необходимо познакомиться с модулями os, sys!
# СМ.: https://pythonworld.ru/moduli/modul-os.html, https://pythonworld.ru/moduli/modul-sys.html

# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
def mk_dirs():
    for i in range(9):
        os.mkdir(os.path.join(os.getcwd(), 'dir_' + str(i + 1)))
        print('Папка %s создана' % ('dir_' + str(i + 1)))
# И второй скрипт, удаляющий эти папки.
 
def rem_dirs():
    for i in range(9):
        os.rmdir('dir_' + str(i + 1))
        print('Папка %s удалена' % ('dir_' + str(i + 1)))

# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.

import os
def show_dirs(path=os.getcwd()):
    if os.listdir(path) != []:
        print('\nТекущая директория содержит:')
        for i in os.listdir(path):
            if os.path.isdir(i):
                print(i)
    else:
        print('\nТекущая директория пуста.')

# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os
def copy_file(path=__file__):
    file = open(path, 'r', encoding='utf-8')
    str = file.read()
    file.close()
    file = open('copy_' + os.path.basename(path), 'w', encoding='utf-8')
    file.write(str)
    file.close()
