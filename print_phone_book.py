import json
def print_phone_book():
    from pprint import pprint
    with open('BD.json', 'r', encoding='utf-8') as f: #открыли файл с данными
        text = json.load(f) #загнали все, что получилось в переменную
        # pprint(text) #вывели результат на экран


        t = text["phone_book"] # ключ от главного словаря
        result = list(map(lambda x : x.get('name'), t)) # обращаемся к списку
        result_2 = list(map(lambda x : x.get('phone'), t))
        # print(result, result_2)
        # for i in range(len(result)): # обращаемся к словарю
        #     print(f"{result[i]}")
        for i in range(len(result)): # обращаемся к словарю
                print(f"{result[i]} {result_2[i]}")
  

        # print(text["phone_book"][0]) # определенный элемент моего пиздеца