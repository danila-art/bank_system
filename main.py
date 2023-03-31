import time
import sys
sys.path.insert(0, "./inner_file")
import autorization
import registration_user


def main():
    hello = "| Добро пожаловать в нашу банковскую систему. |"
    print("-"*len(hello))
    print(f"{hello}")
    print("-"*len(hello))
    arr_control = control_button()
    for element in arr_control:
        print("-"*len(element))
        print(element)
        print("-"*len(element))
    while True:
        select_button = input("Выберете дальнейшее действие: ")
        if (select_button == ""):
            print("Вы ничего не ввели, попробуйте ещё раз")
        elif (select_button.isdigit() == False):
            print("Вы ввели неправильное значение, попробуйте ещё раз...")
        elif (int(select_button) < 1 and int(select_button) > 2):
            print("Вы ввели несуществующее значение")
        elif (int(select_button) == 1):
            # Запуск программы регистрации
            registration_user.registration_user()
            break
        elif (int(select_button) == 2):
            # Запуск программы авторизации
            autorization.autorization_user()
            break


def control_button():
    arr = [
        "| 1 - Зарегистрироваться |",
        "| 2 - Авторизироваться |"
    ]
    return arr


if __name__ == "__main__":
    main()
