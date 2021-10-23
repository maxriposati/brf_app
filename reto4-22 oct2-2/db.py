#importar el modulo sqlite3
import sqlite3
#importar modulo de error de sqlite3
from sqlite3 import Error
from flask import g
#con =sqlite3.connect('database.db')

def get_db():
    try:
        if 'db' not in g:
            g.db=sqlite3.connect('dbase/db_brf.db')
        return g.db
    except Error:
        print(Error)

def close_db():
    db = g.pop('db',None)
    if db is not None:
        db.close()