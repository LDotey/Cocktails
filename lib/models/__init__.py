import sqlite3

CONN = sqlite3.connect('states.db')
CURSOR = CONN.cursor()
