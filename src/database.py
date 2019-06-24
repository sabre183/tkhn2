import sqlite3 as sql
from src.main import filename


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
