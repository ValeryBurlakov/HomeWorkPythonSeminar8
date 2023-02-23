import json

def searchh_contact():
    name_search = input("Введите имя контакта, который хотите найти: ")
    # phone = input("Введите номер: ")
    # new_data = {'id': id, 'name': name, 'phone': phone} #создали переменную, включающую в себя данные, которые мы хотим добавить в уже имеющийся файл

    with open('BD.json', encoding='utf8') as openfile: #Открываем файл
        data = json.load(openfile) #Получае все данные из файла (вообще все, да)
        
        index = 0

    for i in data["phone_book"]:
        if i["name"] == name_search:
            print(i["name"])
            print(i["phone"])


    with open('BD.json', 'w', encoding='utf8') as outfile: #Открываем файл для записи
        json.dump(data, outfile, ensure_ascii=False, indent=2) #Добавляем данные (все, что было ДО добавления данных + добавленные данные)
        # id = id + 1
        # print(f'Контакт {name} успешно добавлен!')
        # return id