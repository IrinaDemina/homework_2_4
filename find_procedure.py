# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os


def get_search(dir_files, current_dir, migrations):
    while True:
        find_list = []
        request = input("Что ищем?:")
        if request.lower() == "stop":
            break
        for file in dir_files:
            if ".sql" in file:
                with open(os.path.join(current_dir, file)) as f:
                    data = f.read()
                    if request.lower() in data.lower():
                        find_list.append(file)
                        print(os.path.join(migrations, file))
        print("Всего: {}".format(len(find_list)))
        dir_files = list(find_list)


def main():
    migrations = 'Migrations'
    current_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), migrations)
    dir_files = os.listdir(current_dir)
    print("Введите 'stop' чтобы закончить")
    get_search(dir_files, current_dir, migrations)


main()
