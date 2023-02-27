# Дополнить телефонный справочник возможностью изменения+ и удаления данных+.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.
import user_interface as ui
import logg_proggram as lg
from datetime import datetime
lg.logging.info('Start program')

def main_():
    dt = datetime.now()
    print(f'\033[1mДоброго времени суток!\033[0m\n{dt.strftime("%A, %d %B %Y %I:%M%p")}')
    while True:
        global command
        command = input("\033[1mВведите команду\033[0m (меню - \033[32m0\033[0m, выход \033[32m9\033[0m): ")
        
        if command == "0":
            # показать меню книги
            ui.menu()
        elif command == "1":
            # вывод телефонной книги
            try:
                import print_phone_book as ppb
                # bd = ui.load_phonebook()
                ppb.printt_phone_book()
            except:
                print("\033[1mУ вас нет контактов. Введите\033[0m \033[32m2\033[0m \033[1mдля добавления первого контакта!\033[0m]")   

        elif command == "2":
            # новый контакт
                import new_contact as new_
                new_.new_contactt()
        elif command == "3":
            # удаление контакта
            import delete_contact as del_
            del_.deletee_contact()
        elif command == "4":
            # поиск контакта
            import search_contact as search_
            search_.searchh_contact()
        elif command == "5":
            # поиск в подстроке(продвинутый поиск)
            import substring_search as ss
            ss.substring_search()
        elif command == "6":
            # BD = ui.save_contact()
            # выгрузка в справочника в файл
            import phone_book_download as download
            download.load()
        elif command == "7":
            # изменение данных
            import change_contact_details as change_
            change_.change_details()
        elif command == "8":
            # копирование справочника
            import copying_a_book as cab
            cab.copy()
        elif command == "9":
            # выход из книги, завершение работы
            print("\033[1mВы завершили работу в телефонной книге\nВсего доброго!\033[0m")
            lg.logging.info('Exit')
            exit()
        else:
            print(f"\033[31mВы ввели отсутствующую команду, повторите \033[0m")
            lg.logging.info('Wrong command')
            ui.menu()
            main_()
main_()