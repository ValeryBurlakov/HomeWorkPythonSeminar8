import json
import logg_proggram as lg
lg.logging.info('Copying')
def copy():
    with open('BD.json', 'r') as f:  # открыли файл с данными
        text = json.load(f)  # загнали все, что получилось в переменную
        # print(text) #вывели результат на экран
        lg.logging.info('Read DATABASE')
        n = input("Введите имя нового файла: ") + '.json'
        n = str(n)

        with open(n, 'w', encoding='utf-8') as openfile:  # Открываем файл
                    # Получаем все данные из файла (вообще все, да)
                    json.dump(text, openfile, ensure_ascii=False, indent=2)
                    print(f"Файл {n} создан, данные скопированы")
                    lg.logging.info('Copying succesfful')