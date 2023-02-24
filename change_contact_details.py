import json


def change_details():
    name_search = input("\033[1mВведите имя контакта, который хотите изменить:\033[0m ")
    # phone = input("Введите номер: ")
    # new_data = {'id': id, 'name': name, 'phone': phone} #создали переменную,
    # включающую в себя данные, которые мы хотим добавить в уже имеющийся файл

    with open('BD.json', encoding='utf8') as openfile:  # Открываем файл
        # Получае все данные из файла (вообще все, да)
        data = json.load(openfile)

    for i in data["phone_book"]:
        if i["name"] == name_search:
            print(i["name"])
            print(i["phone"])
            number = i["phone"]
            email = i["E-mail"]
            surname = i["surname"]
            print("\033[1mкакие данный хотите изменить?\033[0m(ФИО, номер, почту): ")
            answer = int(input("\033[1m1 - ФИО, 2 - номер, почту - 3:\033[0m "))
            if answer == 1:
                answer_name = int(input("1 - имя, 2 - фамилию: "))
                if answer_name == 1:
                    change_name = input(f"\033[1mМеняем имя {name_search} на:\033[0m ")
                    i["name"] = change_name
                    print("Имя изменено")
                elif answer_name == 2:
                    change_name = input(f"Меняем фамилию {surname} на: ")
                    i["surname"] = change_name
                    print("Фамилия изменена")
            elif answer == 2:
                change_phone = input(f"Меняем номер {number} на: ")
                i["phone"] = change_phone
                print(f'Теперь номер контакта {i["name"]}: {i["phone"]}')
            elif answer == 3:
                i["E-mail"] = input(
                    f"Меняем почту контакта {name_search} {surname} с почтой {email} на: ")
        else:
            continue
            # i = i + 1

    with open('BD.json', 'w', encoding='utf8') as outfile:  # Открываем файл для записи
        # Добавляем данные (все, что было ДО добавления данных + добавленные
        # данные)
        json.dump(data, outfile, ensure_ascii=False, indent=2)
        # id = id + 1
        # print(f'Контакт {name} успешно добавлен!')
        # return id
