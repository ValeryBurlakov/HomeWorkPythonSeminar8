# import json
# import os.path
# id = 1

# def create_book():
#     # сохранить в json
#     if os.path.exists("BD.json"):
#         global id
#         name = input("Введите имя: ")
#         surname = input("Введите Фамилию: ")
#         phone = input("Введите номер: ")
#         email = input("Введите почту:")
#         with open('BD.json', encoding='utf8') as openfile:  # Открываем файл
#             # Получаем все данные из файла (вообще все, да)
#             data = json.load(openfile)
#             # создали переменную, включающую в себя данные, которые мы хотим
#             # добавить в уже имеющийся файл
#             new_data = {
#                 'id': id,
#                 'name': name,
#                 "surname": surname,
#                 'phone': phone,
#                 "E-mail": email}
#             if len(data["phone_book"]) <= 1:

#                 data['phone_book'].append(new_data)  # Добавляем данные
#                 print(f'Контакт {name} успешно добавлен!!!!')
#                 with open('BD.json', 'w', encoding='utf8') as outfile:  # Открываем файл для записи
#                     # Добавляем данные (все, что было ДО добавления данных +
#                     # добавленные данные)
#                     json.dump(data, outfile, ensure_ascii=False, indent=2)
#                     print(len(data["phone_book"]))
#     else:         
#         with open('BD.json', 'w', encoding='utf-8') as fh:  # открываем файл на запись
#             BD = {"phone_book": []}
#             fh.write(json.dumps(BD,
#                                 ensure_ascii=False))  # преобразовываем словарь data в unicode-строку и записываем в файл
#             print('Телефонная книга создана1111')
#     create_book()


    