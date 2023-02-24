import json


def load():
    # загрузить из json
    fname = 'BD.json'  # открываем файл
    with open(fname, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
        BD_local = json.load(fh)  # загружаем из файла данные в словарь data
    print('БД успещно загружена')
    return BD_local


BDnew = load()
print(BDnew)
