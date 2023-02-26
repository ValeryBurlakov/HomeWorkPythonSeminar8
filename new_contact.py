import json
import os.path
import logg_proggram as lg
import new_contact as new_
import change_contact_details as change_

id = 1

lg.logging.info('Now')
def new_contactt():
    def added_contact():
        data['phone_book'].append(new_data) #Добавляем данные
        print(f'Контакт {name} успешно добавлен!!!!')
        with open('BD.json', 'w', encoding='utf-8') as outfile: #Открываем файл для записи
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
            t = data["phone_book"] # ключ от главного словаря
            if len(t) > 0:
                name = input("Введите имя: ")
                surname = input("Введите Фамилию: ")
                phone = input("Введите номер: ")
                email = input("Введите почту:")

        
                
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

                pop = list(result_name)
                prop = list(result_surname)
                num = [name, surname]

                if len(t) > 1:
                    for i in range(len(result_name)): # name uniqueness check, если имя уже есть, предложит изменить
                        for j in range(0, len(result_surname)):
                            numb = [result_name[i], result_surname[j]]                    
                    # for i in range(len(result_name)): # name uniqueness check, если имя уже есть, предложит изменить
                    #     for j in range(0, len(result_surname[i])):
                    #         numb = [result_name[i], result_surname[j]]
                            if numb == num:
                                count_fullname += 1

                elif len(t) == 1:
                    for i in result_name[0]:
                        for j in result_surname[0]:
                            numb_ = [result_name[0], result_surname[0]]
                            if num == numb_:
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
                    lg.logging.info('The name is already there')
                    print("такое имя уже есть, добавьте новый контакт(,\nлибо измените имеющийся в соответствующем меню")
            
                
                    # if answer != 1 | answer != 2:
                    #     print("такого пункта нет")

                    answer_user = int(input("\033[1m\033[32m1\033[0m - добавить, \033[32m2\033[0m - изменить, \033[32m3\033[0m - в меню\033[0m: "))
                    if answer_user == 1:
                        new_.new_contactt()
                    elif answer_user == 2:
                        change_.change_details()
                    elif answer_user == 3:
                        print("выходим в меню")
                    else: 
                        print("такого пункта нет, верну вас в меню")


                else:

                    if count_phone > 0:
                        lg.logging.info('the phone number is already there')
                        print("такой номер телефона уже записан, добавьте новый контакт,\nлибо измените имеющийся в соответствующем меню")
                        answer_user = int(input("\033[1m\033[32m1\033[0m - добавить, \033[32m2\033[0m - изменить, \033[32m3\033[0m - в меню\033[0m: "))
                        if answer_user == 1:
                            new_.new_contactt()
                        elif answer_user == 2:
                            change_.change_details()
                        elif answer_user == 3:
                            print("выходим в меню")
                            lg.logging.info('menu exit')
                        else: 
                            print("такого пункта нет, верну вас в меню")
                            lg.logging.info('menu exit')
                        # new_.new_contactt()
                    else:
                        if count_id == 0: # проверка на уникальность id
                            added_contact()
                        else:
                            added_contact("Выходим в меню")
            if len(t) == 0:
                name = input("Введите имя: ")
                surname = input("Введите Фамилию: ")
                phone = input("Введите номер: ")
                email = input("Введите почту:")
                with open('BD.json', encoding='utf8') as openfile:  # Открываем файл
                    # Получаем все данные из файла (вообще все, да)
                    data = json.load(openfile)
                lg.logging.info('Open file')
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
                    lg.logging.info('Added contact succesful')

    else:         
        with open('BD.json', 'w', encoding='utf-8') as fh:  # открываем файл на запись
            BD = {"phone_book": []}
            fh.write(json.dumps(BD,
                                ensure_ascii=False))  # преобразовываем словарь data в unicode-строку и записываем в файл
            lg.logging.info('Create phone book')
            print('\033[1mТелефонная книга создана!\033[0m')

        name = input("Введите имя: ")
        surname = input("Введите Фамилию: ")
        phone = input("Введите номер: ")
        email = input("Введите почту:")
        with open('BD.json', encoding='utf8') as openfile:  # Открываем файл
            # Получаем все данные из файла (вообще все, да)
            data = json.load(openfile)
            lg.logging.info('Open file')
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
                lg.logging.info('Added contact succesful')
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
