import json

BD = {

}

def menu():
    print("0 - вызов меню")
    print("1 - показать справочник")
    print("2 - добавить новый контакт")
    print("3 - удалить контакт")
    print("4 - поиск контакта")
    print("5 - изменение данных")
    print("6 - сохранение данных")
    print("9 - выход из программы")


def load_phonebook():
            # загрузить из json
    fname='BD.json' #открываем файл
    with open(fname, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
        BD_local = json.load(fh)  # загружаем из файла данные в словарь data
    print('БД успещно загружена')
    return BD_local
def print_contacts():   
    for key,value in BD.items():
        print(BD)

# def delete_contact():
#     pass

# def search_contact():
#     pass



# def load():
#             # загрузить из json
#             fname='BD.json' #открываем файл
#             with open(fname, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
#                 BD_local = json.load(fh)  # загружаем из файла данные в словарь data
#             print('БД успещно загружена')
#             return BD_local

def save_contact():
    #  BD = {"phone_book":[]}
    BD = {}
            # сохранить в json
    with open('BD.json', 'w', encoding='utf-8') as fh:  # открываем файл на запись
        fh.write(json.dumps(BD,
            ensure_ascii=False))  # преобразовываем словарь data в unicode-строку и записываем в файл
        print('БД успешно создана')
