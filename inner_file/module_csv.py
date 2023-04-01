# Общий модуль подключения к csv файлам
import csv


def read_csv_user():
    arr_dict_user = []
    with open("./csv/user.csv", 'r', encoding='utf-8') as file:  # Функция данных из файла user.csv
        read = csv.DictReader(file)
        for element in read:
            arr_dict_user.append(element)
    return arr_dict_user


def append_dict_user(dict_user):  # Функция данных из файла user.csv
    with open("./csv/user.csv", 'a', encoding='utf-8', newline="") as file:
        append = csv.DictWriter(file, dict_user)
        append.writerow(dict_user)


def write_new_users(arr_users):  # Функция перезаписи user.csv
    fieldNames = ["surname", "name", "patronomyk", "seria", "number",
                  "date_of_birth", "login", "password", "personal_account", "card", "rang"]
    with open("./csv/user.csv", 'w', encoding='utf-8', newline="") as file:
        write = csv.DictWriter(file, fieldnames=fieldNames)
        write.writeheader()
        for element in arr_users:
            write.writerow(element)
