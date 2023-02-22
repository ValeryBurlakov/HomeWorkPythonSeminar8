import json

def new_contact():
    name = input("Введите имя: ")
    phone = input("Введите номер: ")
    new_data = {'name': name, 'phone': phone} #создали переменную, включающую в себя данные, которые мы хотим добавить в уже имеющийся файл
    with open('BD.json', encoding='utf8') as openfile: #Открываем файл
        data = json.load(openfile) #Получае все данные из файла (вообще все, да)
        data['phone_book'].append(new_data) #Добавляем данные
        with open('BD.json', 'w', encoding='utf8') as outfile: #Открываем файл для записи
            json.dump(data, outfile, ensure_ascii=False, indent=2) #Добавляем данные (все, что было ДО добавления данных + добавленные данные)
        
        print('Контакт успешно добавлен!')