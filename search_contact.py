import json
import logg_proggram as lg

def searchh_contact():

    sname = 'BD.json'  # открываем файл
    with open(sname, 'r', encoding='UTF-8', errors='ignore') as fh:  # открываем файл на чтение

        data = json.load(fh)  # загружаем из файла данные в словарь data
        # json.load(data, fh, ensure_ascii=False, indent=2)
    name_search = input("\033[1mВведите имя контакта, который хотите найти:\033[0m")
    count = 0
    for i in data["phone_book"]:
        if i["name"] == name_search:
            lg.logging.info('contact found')
            print(f'\033[32mname: \033[0m{i["name"]} {i["surname"]} \n' +
                f'\033[32mphone: \033[0m {i["phone"]} \n' +
                f'\033[32mE-mail: \033[0m {i["E-mail"]}\n')  
            count += 1

    if count == 0:
        lg.logging.info('No such contact')
        print("\033[1mТакого контакта нет\033[0m")

    return data



