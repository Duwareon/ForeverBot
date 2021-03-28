#!/usr/bin/env python3
import sqlite3 as sql
from sqlite3 import Error
import typing as t
import gifs


class GifManager():
    def __init__(self):
        self.conn = None
        path = "gifs.db"
        try:
            self.conn = sql.connect(path)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        print("connection complete")

    def get_gifs(self, action, gender: t.Optional[str] = '*'):
        self.cur = self.conn.cursor()

        self.cur.execute(
            'SELECT link FROM GIFS WHERE action = ? AND gender = ?',
            (action, gender,)
        )

        return self.cur.fetchall()
