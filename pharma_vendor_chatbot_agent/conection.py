import sqlite3
import json
try:
    conn = sqlite3.connect('sqlite3.db')
    cursor = conn.cursor()
    print("Conexión exitosa a la base de datos.")
except sqlite3.Error as e:
    print(f"Error al conectar a la base de datos: {e}")
    exit()
# try:
#     cursor.execute("SELECT * FROM medicament")
#     results = cursor.fetchall()  # Obtener todos los resultados
#     #results = cursor.fetchone()  # Obtener solo el primer resultado
#     register_list = [
#         {"id": register[0],
#          "info": {
#                       "nombre": register[1],
#                       "fabricante": register[2],
#                       "precio":register[3],
#                       "description": register[4],
#                       "usos":register[7],
#                       "precio_unitario": register[8],
#                       "cantidad": register[9]
#                       }} for register in results
#         ]
#     with open('medicaments.json', 'w', encoding='utf-8') as json_file:
#         json.dump(register_list, json_file, indent=4, ensure_ascii=False)
#     # resultados = cursor.fetchmany(3) # Obtener los primeros
# except sqlite3.Error as e:
#     print(f"Error al ejecutar la consulta: {e}")
#     exit()