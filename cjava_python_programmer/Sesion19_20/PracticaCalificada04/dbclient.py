import psycopg2
from chat import chat
from datetime import datetime
from pprint import pprint

class dbclient:

    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                "dbname='bd_chat' user='postgres' host='localhost' password='postgresql' port='5432'  "
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            pprint("Conexion exitosa")
            self._create_table()
        except:
            pprint("No se pudo conectar a la base de datos")

    def _create_table(self):
        sql_command = "select count(*) as cnt from pg_tables where tableowner = 'postgres' and tablename = 'cliente';"
        self.cursor.execute(sql_command)
        row = self.cursor.fetchone()                
        
        if  row is not None and int(row[0]) == 0:
            sql_command = """ 
                            CREATE TABLE CLIENTE(
                                ID  SERIAL PRIMARY KEY,
                                CODIGO char(16) not null,
                                NOMBRE_CLI varchar(100),
                                MENSAJE TEXT
                            );
                        """
            #pprint(sql_command)            
            self.cursor.execute(sql_command)        
        
    def insert_new_record(self, cliente):         
        sql_command = """INSERT INTO CLIENTE(codigo, nombre_cli, mensaje)
                         VALUES('%s','%s','%s') """ % ( cliente.codigo, cliente.nombre_cli, cliente.mensaje)
        #pprint(sql_command)
        self.cursor.execute(sql_command)
        return 1