import sqlite3 as sql
from os.path import isdir
from os import mkdir
from os import remove


def filename():
    return r'database\company.db'


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
        # unfinished
