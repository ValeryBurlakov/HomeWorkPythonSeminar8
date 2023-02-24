import json
import new_contact as new_

id = 1

def new_contactt():
    global id

    name = input("Введите имя: ")
    surname = input("Введите Фамилию: ")
    phone = input("Введите номер: ")
    email = input("Введите почту:")

    with open('BD.json', encoding='utf8') as openfile: #Открываем файл
        data = json.load(openfile) #Получаем все данные из файла (вообще все, да)
        
        t = data["phone_book"] # ключ от главного словаря
        result_name = list(map(lambda x : x.get('name'), t))
        result_surname = list(map(lambda x : x.get('surname'), t))
        result_phone = list(map(lambda x : x.get('phone'), t))
        result_email = list(map(lambda x : x.get('E-mail'), t))
        result_id = list(map(lambda x : x.get('id'), t))
        count_fullname = 0
        count_phone = 0
        count_id = 0
        id = max(set(result_id)) + 1
        new_data = {'id': id, 'name': name, "surname": surname, 'phone': phone, "E-mail": email} #создали переменную, включающую в себя данные, которые мы хотим добавить в уже имеющийся файл
        
        for i in result_name:
            for j in result_surname:
                if name == i and surname == j:
                    count_fullname += 1

        for i in result_phone:
            if phone == i:
                count_phone += 1
        
        for i in result_id:
            if id == i:
                count_id += 1
        print(f'count_id {count_id}')
        if count_fullname > 0:
            print("такое имя уже есть, добавьте новый контакт,\nлибо измените имеющийся в соответствующем меню")
            new_.new_contactt()
        else:
            if count_phone > 0:
                print("такой номер телефона уже записан, добавьте новый контакт,\nлибо измените имеющийся в соответствующем меню")
                new_.new_contactt()
            else:
                if count_id == 0:
                    print(f'== 0 {id}')
                    data['phone_book'].append(new_data) #Добавляем данные
                    print(f'Контакт {name} успешно добавлен!')
                    with open('BD.json', 'w', encoding='utf8') as outfile: #Открываем файл для записи
                        json.dump(data, outfile, ensure_ascii=False, indent=2) #Добавляем данные (все, что было ДО добавления данных + добавленные данные)
                    # id = id + 1
                    # return id
                else:
                    data['phone_book'].append(new_data) #Добавляем данные
                    print(f'Контакт {name} успешно добавлен!')
                    with open('BD.json', 'w', encoding='utf8') as outfile: #Открываем файл для записи
                        json.dump(data, outfile, ensure_ascii=False, indent=2) #Добавляем данные (все, что было ДО добавления данных + добавленные данные)
                        with open('numbers.json', 'w', encoding='utf8') as outfile2: #Открываем файл для записи
                            json.dump(data, outfile2, ensure_ascii=False, indent=2) #Добавляем данные (все, что было ДО добавления данных + добавленные данные)
                    # return id



    # id = id + 1
    # return id