import time
import module_csv
import registration_user
import main


def main_admin():
    hello_admin = [
        "Добро пожаловать, Администратор, предоставляю список ваших доступных команд:",
        "| 1 <- Просмотреть базу пользователей.|",
        "| 2 <- Удалить пользователя по лицевому счету. |",
        "| 3 <- Добавить нового Администратора. |",
        "| 0 <- Вернуться в главное меню. |"
    ]
    print("-"*len(hello_admin[0]))
    print(hello_admin[0])
    print("-"*len(hello_admin[0]))
    for el in range(1, 5):
        print("-"*len(hello_admin[el]))
        print(hello_admin[el])
        print("-"*len(hello_admin[el]))
    while True:
        select_operation = input("Введите номер команды: ")
        if (select_operation == ""):
            print("Вы оставили поле пустым,")
        elif (select_operation == '1'):
            # Запуск функции вывода всех клиентов
            print("Запуск функции вывода всех клиентов")
            time.sleep(.5)
            output_all_user()
            pass
        elif (select_operation == '2'):
            # Запуск функции удаления клиента
            print("Запуск функции удаления клиента")
            time.sleep(.5)
            delete_user_to_personal_account()
        elif (select_operation == '3'):
            # Запуск функции добавление нового администратора
            print("Запуск функции добавление нового администратора")
            time.sleep(.5)
            add_new_admin()
        elif (select_operation == '0'):
            # Переход в стартовое меню
            print("Возвращаюсь в стартовое меню...")
            time.sleep(1)
            main.main()
        else:
            print("Вы ввели несуществующее значение")


def add_new_admin():
    surname = registration_user.get_surname()
    name = registration_user.get_name()
    patronomyk = registration_user.get_patronomyk()
    seria = registration_user.get_seria()
    number = registration_user.get_number()
    date_of_birth = registration_user.get_date_of_birth()
    login = registration_user.get_login()
    password = registration_user.get_password()
    personal_account = registration_user.get_personal_account()
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
        "rang": "admin"
    }
    print("Добавление нового адмиинистратора: ->")
    module_csv.append_dict_user(dict_new_user)
    time.sleep(1)
    print("Возвращаюсь в главное меню...")
    time.sleep(1)
    main_admin()


def output_all_user():
    arr_all_users = module_csv.read_csv_user()
    for user in arr_all_users:
        if (user['rang'] == 'user'):
            print(f"Фамилия: {user['surname']} Имя: {user['name']} Отчество: {user['patronomyk']} \nНомер лицевого счета:{user['personal_account']}\n-------------------------------------------")
    main_admin()


def delete_user_to_personal_account():
    del_personal_account = input(
        "Введите лицевой счёт клиента подлежащий удалению: ")
    arr_all_users = module_csv.read_csv_user()
    new_all_users = []
    for user in arr_all_users:
        if (user['personal_account'] == del_personal_account):
            print("Клиент с таким лицевым счетом найден...")
            time.sleep(1)
            print("Удаление выполнено успешно")
        else:
            new_all_users.append(user)
    module_csv.write_new_users(new_all_users)
    print("Возвращаюсь в главное меню администратора-> ")
    time.sleep(1)
    main_admin()
