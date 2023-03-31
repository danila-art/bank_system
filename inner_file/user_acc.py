import module_csv
import time


class user_class:
    surname = None
    name = None
    patronomyk = None
    seria = None
    number = None
    date_of_birth = None
    login = None
    password = None
    personal_account = None
    card = None
    rang = None

    def __init__(self, arr_user):
        self.surname = arr_user[0]
        self.name = arr_user[1]
        self.patronomyk = arr_user[2]
        self.seria = arr_user[3]
        self.number = arr_user[4]
        self.date_of_birth = arr_user[5]
        self.login = arr_user[6]
        self.password = arr_user[7]
        self.personal_account = arr_user[8]
        self.card = arr_user[9]
        self.rang = arr_user[10]

    def hello_user(self):
        print(f"Добро пожаловать, {self.name} {self.patronomyk}")
        print("Производится выгрузка данных -->")
        point = "-"*20
        print(f"{point*3}\nФамилия: {self.surname} | Имя: {self.name} | Отчество: {self.patronomyk}\n{point*3}\nПаспортные данные: {self.seria}-{self.number}\tДата Рождения: {self.date_of_birth}\n{point}\nЛицевой счет -> {self.personal_account}\n{point}")
        if (len(self.card) == 2):
            print("Карты: нет")  # В случае если карт нет
        else:
            # Подключение к файлу карт и вывод всех карт по данным номерам в файле user.csv
            print("Карты есть (Доработать)")

    def system_managment(self):
        arr = [
            "| 1 <-- Получить дебетовую карту |",
            "| 2 <-- Получить кредитную карту |",
            "| 3 <-- Получить кредит наличным |",
            "| 0 <-- Вернуться в главное меню |"
        ]
        for el_arr in arr:
            print("-"*len(el_arr))
            print(el_arr)
            print("-"*len(el_arr))
            time.sleep(.5)

        while True:
            select_operation = input("Выберете что хотите сделать: ")
            if (select_operation == ""):
                print("Вы ничего не указали, повторите ещё раз...")
            elif(select_operation == '1'):
                add_debet_card()  # <- Функция добавления дебетовой карты
                pass          
            elif(select_operation == '2'):
                add_credit_card() # <- Функция добавления кредитной карты
                pass
            elif(select_operation == '3'):
                pass
            elif(select_operation == '0'):
                pass
            else:
                print("Вы ввели несуществующее значение, попробуйте ещё раз")

# Главная функция управления ->
def select_user(get_login, get_password):
    arr_users = module_csv.read_csv_user()
    create_arr_user = []
    for el_user in arr_users:
        if (el_user['login'] == get_login and el_user['password'] == get_password):
            print("Пользователь найден -->")
            for key, value in el_user.items():
                create_arr_user.append(value)
    user = user_class(create_arr_user)
    user.hello_user()
    user.system_managment()
