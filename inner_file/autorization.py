import module_csv
import time
import user_acc
import admin
import main


def autorization_user():
    print("Пожалуйста авторизируйтесь...")
    user_login = get_user_login()
    user_password = get_user_password()
    arr_users = module_csv.read_csv_user()
    for user in arr_users:
        if (user['login'] == user_login and user['password'] == user_password):
            print("Пользователь найден -->")
            if (user['rang'] == "user"):
                time.sleep(1)
                user_acc.select_user(user_login, user_password)
                break
                # Файл пользователя
            elif (user['rang'] == "admin"):
                time.sleep(1)

                # Файл админа
                pass
        else:
            print("Пользователь не найден,зарегистрируйтесь или попробуйте ещё раз...")
            time.sleep(2)
            main.main()


def get_user_login():
    while True:
        user_login = input("Введите Логин: ")
        if (user_login == ""):
            print("Вы оставили пустое поле, пожалуйста попробуйте ещё раз...")
        else:
            return user_login


def get_user_password():
    while True:
        user_password = input("Введите Пароль: ")
        if (user_password == ""):
            print("Вы оставили пустое поле, пожалуйста попробуйте ещё раз...")
        else:
            return user_password
