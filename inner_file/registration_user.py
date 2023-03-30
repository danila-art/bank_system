import module_csv
import random
import main


def registration_user():
    surname = get_surname()
    name = get_name()
    patronomyk = get_patronomyk()
    seria = get_seria()
    number = get_number()
    date_of_birth = get_date_of_birth()
    login = get_login()
    password = get_password()
    personal_account = get_personal_account()
    card = []
    # Формирование словаря -----------
    dict_new_user = {
        "surname": surname,
        "name": name,
        "patronomyk": patronomyk,
        "seria": seria,
        "number": number,
        "date_of_birth": date_of_birth,
        "login": login,
        "password": password,
        "personal_account": personal_account,
        "card": card,
        "rang" : "user"
    }
    print(dict_new_user)
    module_csv.append_dict_user(dict_new_user)
    main.main()


def get_surname():  # Функция добавления surname
    while True:
        input_surname = input("Введите свою Фамилию: ")
        if (input_surname == ''):
            print("Вы ничего не ввели, попробуйте ещё раз")
        else:
            break
    return input_surname


def get_name():  # Функция добавления name
    while True:
        input_name = input("Введите Имя: ")
        if (input_name == ''):
            print("Вы ничего не ввели, попробуйте ещё раз")
        else:
            break
    return input_name


def get_patronomyk():  # Функция добавления patronomyk
    while True:
        input_patronomyk = input("Введите Отчество: ")
        if (input_patronomyk == ''):
            print("Вы ничего не ввели, попробуйте ещё раз")
        else:
            break
    return input_patronomyk


def get_seria():  # Функция добавления seria
    while True:
        input_seria = input("Введите Серию паспорта: ")
        if (input_seria == ''):
            print("Вы ничего не ввели, попробуйте ещё раз")
        elif (len(input_seria) > 4):
            print(
                "Серия паспорт не может быть больше 4 символов, попробуйте ещё раз")
        elif (len(input_seria) < 4):
            print(
                "Серия паспорт не может быть меньше 4 символов, попробуйте ещё раз")
        elif (input_seria.isdigit() == False):
            print("Ваше значение не является числом.")
        else:
            return input_seria
            break


def get_number():  # Функция добавления number
    while True:
        input_number = input("Введите номер паспорта: ")
        if (input_number == ''):
            print("Вы ничего не ввели, попробуйте ещё раз")
        elif (len(input_number) > 6):
            print(
                "Серия паспорт не может быть больше 6 символов, попробуйте ещё раз")
        elif (len(input_number) < 6):
            print(
                "Серия паспорт не может быть меньше 6 символов, попробуйте ещё раз")
        elif (input_number.isdigit() == False):
            print("Ваше значение не является числом.")
        else:
            return input_number
            break


def get_date_of_birth():  # Функция добавления date_of_birth
    while True:
        input_date_of_birth = input("Введите Дату рождения: ")
        if (input_date_of_birth == ''):
            print("Вы ничего не ввели, попробуйте ещё раз")
        else:
            break
    return input_date_of_birth


def get_login():  # Функция добавления login
    input_login = input("Введите Логин: ")
    if (input_login != ''):
        arr_user = module_csv.read_csv_user()
        for element in arr_user:
            if (element['login'] == input_login):
                print("Извините но такой логин уже существует")
                get_login()
            else:
                print("Совпадений не найдено")
                return input_login
    else:
        print("Вы ничего не ввели, попробуйте ещё раз")
        get_login()


def get_password():  # Функция добавления password
    while True:
        input_password = input("Введите Пароль: ")
        if (input_password == ''):
            print("Вы ничего не ввели, попробуйте ещё раз")
        else:
            break
    return input_password


def get_personal_account():  # Функция добавления personal_account
    personal = "s-2202"
    personal_int = random.randint(1000, 9999)
    arr_dict_users = module_csv.read_csv_user()
    for element in arr_dict_users:
        arr_del = str(element['personal_account']).split('s-2202')
        print(arr_del)
        if(int(arr_del[1]) == personal_int):
            get_personal_account() #если найдено совпадение, перезапуск функции
        else:
            input_personal_account = personal + str(personal_int)
            return input_personal_account
