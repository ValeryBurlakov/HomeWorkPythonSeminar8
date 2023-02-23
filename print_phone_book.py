import json
def print_phone_book():
    from pprint import pprint
    with open('BD.json', 'r', encoding='utf-8') as f: #открыли файл с данными
        text = json.load(f) #загнали все, что получилось в переменную
        # pprint(text) #вывели результат на экран


        t = text["phone_book"] # ключ от главного словаря
        result = list(map(lambda x : x.get('name'), t)) # обращаемся к списку получаем name
        result_2 = list(map(lambda x : x.get('phone'), t)) # получаем phone
        result_3 = list(map(lambda x : x.get('surname'), t))
        # print(result, result_2)
        # for i in range(len(result)): # обращаемся к словарю
        #     print(f"{result[i]}")
        # print(len(result))
        for i in range(len(result)): # обращаемся к словарю
                print(f"{i + 1}\033[32m name: \033[0m{result[i]} {result_3[i]} \n" + f'\033[32mphone: \033[0m {result_2[i]}')
                print()
  

        # print(text["phone_book"][0]) # определенный элемент моего пиздеца