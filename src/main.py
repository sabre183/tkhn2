import os
from os.path import isdir
from src.databaseClass import filename, Database
from src.menuControl import menu_control


def start_init():
    try:
        if not os.path.isfile(filename()):
            raise FileNotFoundError
    except FileNotFoundError:
        create_db()
    finally:
        print("Database is ready to use.")


def create_db():
    print("Database does not exist. Check if the file exists and is in proper directory.")
    print("Enter 'y' if you want to create a new database, enter any other key if you want to abort.")
    if input(">>> ").lower() == 'y':
        if isdir('database'):
            os.mkdir('database')
        f = open(filename(), "+w").close()
        print("File created.")
        with Database() as db:
            # job info
            db.cursor.execute("create table dept("
                              "deptno number autoincrement,"  # ID # TODO: THIS FIELD IS WRONG. FIX IT FAM. 
                              "dname varchar2(14), "  # name of department
                              "loc varchar2(13),"
                              "constraint ID primary key (deptno));")  # location of department
            print("Department table created.")
            db.cursor.execute("create table emp("
                              "empno number,"
                              "empname varchar2(10),"
                              "empsurname varchar2(10),"
                              "job varchar2(10),"
                              "hiredate date,"
                              "salary number,"
                              "deptno number,"
                              "constraint fk_deptno foreign key (deptno) references dept (deptno),"
                              "constraint emp_id primary key (empno));")
            print("Worker table created.")
            print("Testing database...")
            if db.test_db() != 0:
                print("Database testing has failed. Aborting program...")
                os.remove(filename())
                exit(1)
            else:
                print("Database has been created.")
    else:
        print("Cannot proceed without database; aborted.")
        exit(1)


def main():
    start_init()
    main_menu()


def main_menu():
    while True:
        print("1 - Worker Management\n"
              "Q - Exit Program")
        input_dict = {'1': 'workers.worker_menu()', 'q': 'exit(0)'}
        return menu_control(input_dict)


if __name__ == "__main__":
    main()
