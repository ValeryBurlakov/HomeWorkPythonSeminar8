import json
import os.path 
import logg_proggram as lg
import new_contact as new_
import change_contact_details as change_

id = 1
# def add_book():
#     with open('BD.json', 'w', encoding='utf-8') as fh:  # открываем файл на запись
#         BD = {"phone_book": []}
#         fh.write(json.dumps(BD,
#                             ensure_ascii=False))  # преобразовываем словарь data в unicode-строку и записываем в файл
#         print('Телефонная книга создана')
        
def new_contactt():
    def added_contact():
        data['phone_book'].append(new_data) #Добавляем данные
        print(f'Контакт {name} успешно добавлен!!!!')
        with open('BD.json', 'w', encoding='utf8') as outfile: #Открываем файл для записи
            json.dump(data, outfile, ensure_ascii=False, indent=2) #Добавляем данные (все, что было ДО добавления данных + добавленные данные)
            lg.logging.info('Added contact succesfull')

    def answer():
        if answer == 1:
            new_.new_contactt()
        elif answer == 2:
            change_.change_details()

    global id

    if os.path.exists("BD.json"):
        with open('BD.json', encoding='utf8') as openfile: #Открываем файл
            data = json.load(openfile) #Получаем все данные из файла (вообще все, да)
            name = input("Введите имя: ")
            surname = input("Введите Фамилию: ")
            phone = input("Введите номер: ")
            email = input("Введите почту:")

    
        
            t = data["phone_book"] # ключ от главного словаря
            result_name = list(map(lambda x : x.get('name'), t))
            result_surname = list(map(lambda x : x.get('surname'), t))
            result_phone = list(map(lambda x : x.get('phone'), t))
            result_email = list(map(lambda x : x.get('E-mail'), t))
            result_id = list(map(lambda x : x.get('id'), t))
            count_fullname = 0
            count_phone = 0
            count_id = 0
            count_email = 0
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
            for i in result_email:
                if id == i:
                    count_email += 1

            if count_fullname > 0:
                print("такое имя уже есть, добавьте новый контакт(,\nлибо измените имеющийся в соответствующем меню")
            
                
                # if answer != 1 | answer != 2:
                #     print("такого пункта нет")

                answer_user = int(input("1 - добавить, 2 - изменить, 3 - в меню: "))
                if answer_user == 1:
                    new_.new_contactt()
                elif answer_user == 2:
                    change_.change_details()
                else: 
                    print("такого пункта нет, верну вас в меню")


            else:

                if count_phone > 0:
                    print("такой номер телефона уже записан, добавьте новый контакт,\nлибо измените имеющийся в соответствующем меню")
                    new_.new_contactt()
                else:
                    if count_id == 0: # проверка на уникальность id
                        added_contact()
                    else:
                        added_contact()
    else:         
        with open('BD.json', 'w', encoding='utf-8') as fh:  # открываем файл на запись
            BD = {"phone_book": []}
            fh.write(json.dumps(BD,
                                ensure_ascii=False))  # преобразовываем словарь data в unicode-строку и записываем в файл
            print('\033[1mТелефонная книга создана!\033[0m')

        name = input("Введите имя: ")
        surname = input("Введите Фамилию: ")
        phone = input("Введите номер: ")
        email = input("Введите почту:")
        with open('BD.json', encoding='utf8') as openfile:  # Открываем файл
            # Получаем все данные из файла (вообще все, да)
            data = json.load(openfile)
            # создали переменную, включающую в себя данные, которые мы хотим
            # добавить в уже имеющийся файл
            new_data = {
                'id': id,
                'name': name,
                "surname": surname,
                'phone': phone,
                "E-mail": email}
            if len(data["phone_book"]) <= 1:
                added_contact()
                # data['phone_book'].append(new_data)  # Добавляем данные
                # print(f'Контакт {name} успешно добавлен!!!!')
                # with open('BD.json', 'w', encoding='utf8') as outfile:  # Открываем файл для записи
                #     json.dump(data, outfile, ensure_ascii=False, indent=2)
                lg.logging.info('Added contact succesfull')
                    # print(len(data["phone_book"]))




    
# ===========
# def new_contactt():
#     global id

#     name = input("Введите имя: ")
#     surname = input("Введите Фамилию: ")
#     phone = input("Введите номер: ")
#     email = input("Введите почту:")

#     with open('BD.json', encoding='utf8') as openfile: #Открываем файл
#         data = json.load(openfile) #Получаем все данные из файла (вообще все, да)
        
#         t = data["phone_book"] # ключ от главного словаря
#         result_name = list(map(lambda x : x.get('name'), t))
#         result_surname = list(map(lambda x : x.get('surname'), t))
#         result_phone = list(map(lambda x : x.get('phone'), t))
#         result_email = list(map(lambda x : x.get('E-mail'), t))
#         result_id = list(map(lambda x : x.get('id'), t))
#         count_fullname = 0
#         count_phone = 0
#         count_id = 0
#         count_email = 0
#         id = max(set(result_id)) + 1
#         new_data = {'id': id, 'name': name, "surname": surname, 'phone': phone, "E-mail": email} #создали переменную, включающую в себя данные, которые мы хотим добавить в уже имеющийся файл
        
#         def added_contact():
#             data['phone_book'].append(new_data) #Добавляем данные
#             print(f'Контакт {name} успешно добавлен!!!!')
#             with open('BD.json', 'w', encoding='utf8') as outfile: #Открываем файл для записи
#                 json.dump(data, outfile, ensure_ascii=False, indent=2) #Добавляем данные (все, что было ДО добавления данных + добавленные данные)

#         for i in result_name:
#             for j in result_surname:
#                 if name == i and surname == j:
#                     count_fullname += 1

#         for i in result_phone:
#             if phone == i:
#                 count_phone += 1
        
#         for i in result_id:
#             if id == i:
#                 count_id += 1
#         for i in result_email:
#             if id == i:
#                 count_email += 1

#         if count_fullname > 0:
#             print("такое имя уже есть, добавьте новый контакт,\nлибо измените имеющийся в соответствующем меню")
#             new_.new_contactt()
#         else:
#             if count_phone > 0:
#                 print("такой номер телефона уже записан, добавьте новый контакт,\nлибо измените имеющийся в соответствующем меню")
#                 new_.new_contactt()
#             else:
#                 if count_id == 0: # проверка на уникальность id
#                     added_contact()
#                 else:
#                     added_contact()
