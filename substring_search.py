import json
import logg_proggram as lg
lg.logging.info('substring search contact')
def substring_search():
        with open('BD.json', encoding='utf8') as openfile: #Открываем файл
            data = json.load(openfile) #Получаем все данные из файла (вообще все, да)
        t = data["phone_book"]

        name_search = input("Вводите данные контакта: ")
        name_search = str.title(name_search)
        result_name = list(map(lambda x : x.get('name'), t))
        result_surname = list(map(lambda x : x.get('surname'), t))
        result_phone = list(map(lambda x : x.get('phone'), t))
        result_email = list(map(lambda x : x.get('E-mail'), t))
        result_id = list(map(lambda x : x.get('id'), t))
        names = list(result_name)
        surnames = list(result_surname)

        names_list_index = []
        
        # print(result_name)
        count = 0

        for rn in result_name:
            rn = result_name[count]
            rsn = result_surname[count]
            sn = result_surname[count]
            nrp = result_phone[count]
            nre = result_email[count]
            nri = result_id[count]

            if name_search in rn or name_search in sn or name_search in nrp or name_search in nre:
                names_list_index.append(count)
                print(f'Возможно вы искали: {rn} {rsn}')
                count += 1
            else:
                count += 1
        
        if count == 0:
            lg.logging.info('No such contact')
            print("\033[1mТакого контакта нет!!!\033[0m")




        # print(f'Идексы имен {names_list_index}')
        # count_surname = 0

        # for i in result_surname:
        #     sn = result_surname[count_surname]
        #     n = result_name[count_surname]
        #     if name_search in sn:
        #         surnames_list_index.append(count_surname)
        #         print(f'Возможно вы искали: {n} {sn}')
        #         count_surname += 1
        #     else:
        #          count_surname += 1
        #     # elif name_search not in sn:
        #     #     count_surname += 1
        #     if count_surname == 0:      
        #         print("нет контакта с такими данными")
        # print(f'Идексы фамилий {surnames_list_index}')
        # print(result_name) # повторяющиеся значения
        # dup = [x for i, x in enumerate(result_name) if i != names_list.index(x)]
        # print(dup)

    

    # sname = 'BD.json'  # открываем файл
    # with open(sname, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
    #     data = json.load(fh)  # загружаем из файла данные в словарь data
    #     phone_book = data["phone_book"]


    #     foundkeys = []
    #     for keys in phone_book:
    #         for i in 
    #         if phone_book[keys] == name_search:
    #             foundkeys.append(keys)
    #     print(foundkeys)
    #     return foundkeys
    
    

    # count = 0
    # for i in data["phone_book"]:
    #     if i["name"] == name_search:
    #         lg.logging.info('contact found')
    #         print(f'{i["name"]} {i["surname"]}')
    #         print(f'{i["phone"]}\n')
    #         count += 1

    # if count == 0:
    #     lg.logging.info('No such contact')
    #     print("Такого контакта нет")

    # return data