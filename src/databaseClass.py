import sqlite3 as sql
from os.path import isdir
from os import mkdir
from os import remove


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
                remove(filename)
                exit(1)
            else:
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

    def test_db(self):
        with self as db:
            test_dept = {986, 'MAIN', 'WARSAW'}
            db.cursor.execute("insert into dept values(?,?,?)", test_dept)
            if db.cursor.execute("select * from dept") != test_dept:
                print("Problem during testing database - may not be empty or not readable.")
                db.cursor.execute("delete from dept where deptno == 986;")
                return 1
