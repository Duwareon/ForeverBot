#!/usr/bin/env python3
import sqlite3 as sql
from sqlite3 import Error
from typing import Optional
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

    def get_gifs(self, action, gender: Optional[str] = "*"):
        cur = self.conn.cursor()

        cur.execute(
            self.conn.escape_string(
                "SELECT link FROM GIFS WHERE action = '{0}' AND gender = '{1}'".format(
                    action, gender)))

        links = cur.fetchall()

        return links[0]
