import os
from src.databaseClass import create_db, filename
from src.menuControl import menu_control


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


def main_menu():
    print("1 - Worker Management\n"
          "Q - Exit Program")
    input_dict = {'1': 'workers.worker_menu()', 'q': 'exit(0)'}
    menu_control(input_dict)


if __name__ == "__main__":
    main()
