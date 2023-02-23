import json

def change_details():
    name_search = input("Введите имя контакта, который хотите изменить: ")
    # phone = input("Введите номер: ")
    # new_data = {'id': id, 'name': name, 'phone': phone} #создали переменную, включающую в себя данные, которые мы хотим добавить в уже имеющийся файл

    with open('BD.json', encoding='utf8') as openfile: #Открываем файл
        data = json.load(openfile) #Получае все данные из файла (вообще все, да)
        
   

    for i in data["phone_book"]:
        if i["name"] == name_search:
            print(i["name"])
            print(i["phone"])
            number = i["phone"] 
            det = input("какие данный хотите изменить?(имя, номер): ")
            if det == "имя":
                change_name = input(f"Меняем имя {name_search} на: ")
                i["name"] = change_name
                print(i["name"])
            elif det == "номер":
                change_phone = input(f"Меняем номер {number} на: ")
                i["phone"] = change_phone
                print(f'Теперь номер контакта {i["name"]}: {i["phone"]}')
        else:
            continue
            # i = i + 1

    
    with open('BD.json', 'w', encoding='utf8') as outfile: #Открываем файл для записи
        json.dump(data, outfile, ensure_ascii=False, indent=2) #Добавляем данные (все, что было ДО добавления данных + добавленные данные)
        # id = id + 1
        # print(f'Контакт {name} успешно добавлен!')
        # return id