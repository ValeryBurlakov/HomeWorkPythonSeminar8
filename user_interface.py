import json

BD = {}


def menu():
    print("\033[32m0\033[0m - вызов меню")
    print("\033[32m1\033[0m - показать справочник")
    print("\033[32m2\033[0m - добавить новый контакт")
    print("\033[32m3\033[0m - удалить контакт")
    print("\033[32m4\033[0m - поиск контакта")
    print("\033[32m5\033[0m - изменение данных")
    print("\033[32m6\033[0m - выгрузка данных")
    print("\033[32m9\033[0m - выход из программы")


def load_phonebook():
    # загрузить из json
    fname = 'BD.json'  # открываем файл
    with open(fname, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
        BD_local = json.load(fh)  # загружаем из файла данные в словарь data
    print('БД успещно загружена')
    return BD_local


def save_contact():
    BD = {"phone_book": []}
    # BD = {}
    # сохранить в json
    with open('BD.json', 'w', encoding='utf-8') as fh:  # открываем файл на запись
        fh.write(json.dumps(BD,
                            ensure_ascii=False))  # преобразовываем словарь data в unicode-строку и записываем в файл
        print('БД успешно создана')
