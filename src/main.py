import os
from src.workers import worker_menu
from src.databaseClass import create_db


def start_init():
    try:
        if not os.path.isfile(filename()):
            raise FileNotFoundError
    except FileNotFoundError:
        create_db()
    finally:
        print("Database is ready to use.")


def main():
    start_init()
    main_menu()


def filename():
    return '/database/company.db'


if __name__ == "__main__":
    main()


def main_menu():
    input_dict = {1: "worker_menu()", }
    while True:
        print_main_menu()
        choice = input(">>> ")
        if choice in input_dict:
            main_menu_control(choice)
        else:
            print("Invalid selection. Try again. \n")


def main_menu_control(choice):
    if choice == 1:
        worker_menu()


def print_main_menu():
    print("1 - Worker management")
