import json

def deletee_contact():
    name_del = str(input("Введите имя контакта, который хотите удалить: "))
    
    with open('BD.json', encoding='utf8') as openfile: #Открываем файл
        data = json.load(openfile) #Получае все данные из файла (вообще все, да)

    index = 0

    for i in data["phone_book"]:
        if i["name"] == name_del:
            data["phone_book"].pop(index)
        else:
            index += 1

    with open('BD.json', 'w', encoding='utf8') as outfile: #Открываем файл для записи
            json.dump(data, outfile, ensure_ascii=False, indent=2) #Добавляем данные (все, что было ДО добавления данных + добавленные данные)
        
    print('Контакт успешно удалён!')