import os
import sqlite3

filename = '/database/company.db'


def start_init():
    try:
        if not os.path.isfile(filename):
            raise FileNotFoundError
    except FileNotFoundError:
        print("Database does not exist. Check if the file exists and is in proper directory.")
        print("Enter 'y' if you want to create a new database, enter any other key if you want to abort.")
        if input(">>>").lower() == 'y':
            open(filename).close()
            print("Database has been created.")



def main():
    start_init()


if __name__ == "__main__":
    main()


def main_menu():
    print()
