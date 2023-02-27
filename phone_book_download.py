import json
import logg_proggram as lg

def load():
    # загрузить из json
    fname = 'BD.json'  # открываем файл
    with open(fname, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
        BD_local = json.load(fh)  # загружаем из файла данные в словарь data
        lg.logging.info('Read DATABASE')
    print('\033[1mБД успещно загружена\033[0m')
    return BD_local


BDnew = load()
print(BDnew)
