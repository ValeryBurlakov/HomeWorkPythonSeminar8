import user_interface as ui

while True:
    command = input("Введите команду (меню - 0, выход 9): ")
    if command == "0":
        # показать меню книги
        ui.menu()
    elif command == "1":
        # вывод телевонной книги
        try:
            import print_phone_book as ppb
            # bd = ui.load_phonebook()
            ppb.print_phone_book()
        except:
            print("База данных не найдена")
    elif command == "2":
        # новый контакт
        import new_contact as new_
        new_.new_contactt()
    elif command == "3":
        # удаление контакта
        import delete as del_
        del_.deletee_contact()
    elif command == "4":
        # поиск контакта
        import search_contact as search_
        search_.searchh_contact()
    elif command == "5":
        # изменение данных
        import change_contact_details as change_
        change_.change_details()
    elif command == "6":
        BD = ui.save_contact() 
    elif command == "9":
        # выход из книги, завершение работы
        print("Вы завершили работу в телефонной книге\nВсего доброго!")
        exit()