import os
from src.workers import worker_menu


def start_init():
    try:
        if not os.path.isfile(filename):
            raise FileNotFoundError
    except FileNotFoundError:
        print("Database does not exist. Check if the file exists and is in proper directory.")
        print("Enter 'y' if you want to create a new database, enter any other key if you want to abort.")
        if input(">>> ").lower() == 'y':
            open(filename).close()
            print("Database has been created.")
    finally:
        print("Database is ready to use.")


def main():
    start_init()
    main_menu()


if __name__ == "__main__":
    filename = '/database/company.db'
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
