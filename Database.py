"""
    Database
    Author: Alex Lambert
"""
import sqlite3


class DataBase(object):
    def __init__(self):
        self.conn = sqlite3.connect("Database")
        self.cursor = self.conn.cursor()
        self.intializeTables()

    def intializeTables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS TRAILS
                            (ID TEXT PRIMARY KEY     NOT NULL,
                            NAME                      TEXT    NOT NULL,
                            DISTANCE                  TEXT    NOT NULL,
                            GAIN                      TEXT    NOT NULL,
                            HIGH                      TEXT    NOT NULL);''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS USERS
                            (ID INT PRIMARY KEY     NOT NULL,
                            NAME            TEXT    NOT NULL,
                            DISTANCE        TEXT    NOT NULL,
                            GAIN            TEXT    NOT NULL,
                            HIGH            TEXT    NOT NULL);''')

