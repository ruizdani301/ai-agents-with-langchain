import sqlite3
def get_conection():
    try:
        return sqlite3.connect('sqlite3.db')
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        exit()
