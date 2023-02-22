import user_interface as ui

while True:
    command = input("Введите команду (меню - 0, выход 9): ")
    if command == "0":
        ui.menu()
    elif command == "1":
        try:
            import print_phone_book as ppb
            # bd = ui.load_phonebook()
            ppb.print_phone_book()
        except:
            print("База данных не найдена")
    elif command == "8":
        import new_contact
        new_contact.new_contact()
    elif command == "3":
        ui.delete_contact()
        print("Здесь будет удаление контакта")
    elif command == "4":
        print("Здесь будет поиск контакта")
    elif command == "5":
        print("Здесь будет изменение данных")
    elif command == "6":
        BD = ui.save_contact() 
    elif command == "9":
        exit()