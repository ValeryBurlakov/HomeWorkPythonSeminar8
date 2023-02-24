import json


def printt_phone_book():

    with open('BD.json', 'r', encoding='utf-8') as f:  # открыли файл с данными
        text = json.load(f)  # загнали все, что получилось в переменную
        # pprint(text) #вывели результат на экран

    t = text["phone_book"]  # ключ от главного словаря с данными контактов
    # обращаемся к словарю получаем список имён
    list_name = list(map(lambda x: x.get('name'), t))
    list_phone = list(map(lambda x: x.get('phone'), t)
                      )  # получаем номера телефонов
    list_surname = list(map(lambda x: x.get('surname'), t))  # получаем фамилии
    list_email = list(map(lambda x: x.get('E-mail'), t)
                      )  # получаем адреса почты
    # print(t)

    for i in range(len(list_name)):
        if list_email[i] is None:
            print(
                f"\033[1m{i + 1}\033[0m \033[32mname: \033[0m{list_name[i]} {list_surname[i]} \n" +
                f'\033[32mphone: \033[0m {list_phone[i]}\n')
        else:
            print(
                f"\033[1m{i + 1}\033[0m \033[32mname: \033[0m{list_name[i]} {list_surname[i]} \n" +
                f'\033[32mphone: \033[0m {list_phone[i]} \n' +
                f'\033[32mE-mail: \033[0m {list_email[i]}\n')

    # for i in range(len(list_name)): # обращаемся к списку имён
    #     print(f"{i + 1}\033[32m name: \033[0m{list_name[i]} {list_surname[i]} \n" + f'\033[32mphone: \033[0m {list_phone[i]} \n' + f'\033[32mE-mail: \033[0m {list_email[i]}')
    #     print()

    # print(text["phone_book"][0]) # определенный элемент моего пиздеца
