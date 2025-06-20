import json
from conection import cursor, conn


def update_json():
    """
    Updates the JSON file with records from the database.

    Connects to the database, executes a query to retrieve all records from the
    'medicament' table, and saves them into a file named 'medicaments.json'.

    The file is created in the same directory as the script,
    If an error occurs during the query execution, the error message is printed
    and the program exits.
    """

    try:
        cursor.execute("SELECT * FROM medicament")
        results = cursor.fetchall()
        # register_list = [
        #     {"id": register[0],
        #      "info": {
        #                 "nombre": register[1],
        #                 "fabricante": register[2],
        #                 "precio":register[3],
        #                 "description": register[4],
        #                 "usos":register[7],
        #                 "precio_unitario": register[8],
        #                 "cantidad": register[9]
        #                 }} for register in results
        #     ]
        register_to_vector = []
        for register in results:
            string_register = (
                                f"id:{register[0]}, "
                                f"nombre:{register[1]}, "
                                f"fabricante:{register[2]}, "
                                f"precio:{register[3]}, "
                                f"descripcion:{register[4]}, "
                                f"usos:{register[7]}, "
                                f"precio_unitario:{register[8]}, "
                                f"cantidad_disponible:{register[9]}"
                            )
            register_to_vector.append(string_register)
        with open('medicaments.json', 'w', encoding='utf-8') as json_file:
            json.dump(register_to_vector, json_file, ensure_ascii=False)
    except conn.Error as e:
        print(f"Error al ejecutar la consulta: {e}")
        exit()
