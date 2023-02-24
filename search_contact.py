import json


def searchh_contact():
    name_search = input("Введите имя контакта, который хотите найти: ")

    sname = 'BD.json'  # открываем файл
    with open(sname, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
        data = json.load(fh)  # загружаем из файла данные в словарь data

    count = 0
    for i in data["phone_book"]:
        if i["name"] == name_search:

            print(f'{i["name"]} {i["surname"]}')
            print(f'{i["phone"]}\n')
            count += 1

    if count == 0:
        print("Такого контакта нет")

    return data
