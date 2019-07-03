import sqlite3 as sql
from os.path import isdir
from os import mkdir


def filename():
    return r'database\company.db'


def create_db():
    print("Database does not exist. Check if the file exists and is in proper directory.")
    print("Enter 'y' if you want to create a new database, enter any other key if you want to abort.")
    if input(">>> ").lower() == 'y':
        if isdir('database'):
            mkdir('database')
        f = open(filename(), "+w").close()
        print("File created.")
        with Database() as db:
            # job info
            db.cursor.execute("create table dept("
                              "deptno number,"  # ID # TODO: THIS FIELD IS WRONG. FIX IT FAM. 
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
            db.cursor.execute()
            print("Database has been created.")
    else:
        print("Cannot proceed without database; aborted.")
        exit(1)


class Database:
    def __init__(self):
        self._conn = sql.connect(filename())
        self._cursor = self._conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self._conn.close()

    @property
    def cursor(self):
        return self._cursor

    @property
    def connection(self):
        return self._conn

    def commit(self):
        self.connection.commit()

    def new_worker(self):
        with self as db:
            db.cursor.execute("")
