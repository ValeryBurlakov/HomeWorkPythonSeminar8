import json
import logg_proggram as lg

lg.logging.info('substring search contact')
def substring_search():
        with open('BD.json', encoding='utf8') as openfile:
            data = json.load(openfile)
            t = data["phone_book"]

        name_search = input("\033[1mВведите данные контакта:\033[0m ")
        name_search = str.title(name_search)
        result_name = list(map(lambda x : x.get('name'), t))
        result_surname = list(map(lambda x : x.get('surname'), t))
        result_phone = list(map(lambda x : x.get('phone'), t))
        result_email = list(map(lambda x : x.get('E-mail'), t))
        result_id = list(map(lambda x : x.get('id'), t))
        # names = list(result_name)
        # surnames = list(result_surname)
        
        names_list_index = []
        count = 0

        for i in result_name:

            rn = result_name[count]
            rsn = result_surname[count]
            sn = result_surname[count]
            nrp = result_phone[count]
            nre = (result_email[count])
            # name_search_l = name_search.lower()
            nri = result_id[count]

            if name_search in rn or name_search in sn:
                names_list_index.append(count)
                print(f'\033[1mВозможно вы искали:\033[0m {rn} {rsn}, \033[1mID\033[0m - \033[32m{nri}\033[0m')
                count += 1
                lg.logging.info('contact found')
            elif name_search in nrp or name_search.lower() in nre.lower():
                names_list_index.append(count)
                print(f'\033[1mВозможно вы искали:\033[0m {rn} {rsn}, \033[1mmail\033[0m: {nre}, \033[1mID\033[0m - \033[32m{nri}\033[0m')
                count += 1
                lg.logging.info('contact found')
            else:
                count += 1

        if len(names_list_index) == 0:
            lg.logging.info('No such contact')
            print("\033[1mТакого контакта нет!!!\033[0m")
        elif len(names_list_index) > 0:
            id_search = int(input("\033[1mВведите\033[0m \033[32mID\033[0m \033[1mконтакта для вывода подробной информации о нём,\033[0m \033[32m0\033[0m - \033[1mвыход в меню:\033[0m "))
            found = 0
            if id_search == 0:
                print("\033[1mвыходим в меню\033[0m")
                lg.logging.info('menu exit')
                found = 1
            for i in t:
                if i["id"] == id_search:
                    print(f'\033[32mname: \033[0m{i["name"]} {i["surname"]} \n' +
                    f'\033[32mphone: \033[0m {i["phone"]} \n' +
                    f'\033[32mE-mail: \033[0m {i["E-mail"]}')
                    lg.logging.info('full output')
                    found += 1
                    return found
            if found == 0:
                print(f"\033[1mКонтакт с id\033[0m - \033[32m{id_search}\033[0m \033[1mотсутствует в телефонной книге!\033[0m]")
                lg.logging.info('contact not found')