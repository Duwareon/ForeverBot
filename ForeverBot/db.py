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
        check = {"ff", "mf", "mm"}
        if any(ext in gender for ext in check):
            self.cur.execute(
                'SELECT link FROM GIFS WHERE action = ? AND gender = ?',
                (action, gender,)
            )
        else:
            self.cur.execute(
                'SELECT link FROM GIFS WHERE action = ?',
                (action,)
            )

        print(self.cur.fetchall())
        return self.cur.fetchall()
