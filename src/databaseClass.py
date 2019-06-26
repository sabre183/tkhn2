import sqlite3 as sql
from src.main import filename


def create_db():
    print("Database does not exist. Check if the file exists and is in proper directory.")
    print("Enter 'y' if you want to create a new database, enter any other key if you want to abort.")
    if input(">>> ").lower() == 'y':
        with Database() as db:
            # job info
            db.cursor.execute("create table dept("
                              "deptno number,"
                              "constraint ID primary key (deptno)," # ID
                              "dname varchar2(14), " # name of department
                              "loc varchar2(13));") # location of department
            db.cursor.execute("")
            print("Database has been created.")
    else:
        print("Cannot proceed without database; aborted.")
        exit(1)


class Database:
    def __init__(self):
        self._conn = sql.connect(filename)
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

