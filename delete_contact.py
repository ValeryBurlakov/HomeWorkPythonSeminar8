import json
import logg_proggram as lg

def deletee_contact():
    name_del = str(input("Введите имя контакта, который хотите удалить: "))
    

    with open('BD.json', encoding='utf8') as openfile:  # Открываем файл
        # Получае все данные из файла (вообще все, да)
        data = json.load(openfile)
        lg.logging.info('Open file')

    index = 0
    
    items = data.values()
    print(items)    
    for i in data["phone_book"]:
        if i["name"] == name_del:
            print(f'{i["name"]} {i["surname"]}')
            data["phone_book"].pop(index)
        else:
            index += 1

    with open('BD.json', 'w', encoding='utf8') as outfile:  # Открываем файл для записи
        # Добавляем данные (все, что было ДО добавления данных + добавленные
        # данные)
        json.dump(data, outfile, ensure_ascii=False, indent=2)
        lg.logging.info('Delete contact')
        lg.logging.info('Data recording')
    print('Контакт успешно удалён!')
