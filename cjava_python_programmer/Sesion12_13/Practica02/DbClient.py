import psycopg2
from Persona import Persona
from pprint import pprint

class DbClient:

    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                "dbname='personas' user='postgres' host='localhost' password='postgresql' port='5432'  "                
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            pprint("Conexion exitosa")
        except:
            pprint("No se pudo conectar a la base de datos")
        
    def insert_new_record(self, objpersona):         
        insert_command = """INSERT INTO persona(id, dni, nombre, apellido, direccion, telefono)
                          VALUES(nextval('personas_sequence'), '%s','%s','%s','%s','%s') """ % ( objpersona.dni, objpersona.nombre, objpersona.apellido, objpersona.direccion, objpersona.telefono)
        pprint(insert_command)
        self.cursor.execute(insert_command)
        return 1