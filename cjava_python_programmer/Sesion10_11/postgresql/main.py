import psycopg2
from pprint import pprint

class DatabaseConnection:
    
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                "dbname='posgresdemo' user='postgres' host='localhost' password='postgresql' port='5432'  "                
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            pprint("Conexión exitosa")
        except:
            pprint("No se pudo conectar a la base de datos")
    
    def create_table(self):
        create_table_command = "CREATE TABLE pet(id serial PRIMARY KEY, name varchar(100), age integer NOT NULL)"
        self.cursor.execute(create_table_command)

    def insert_new_record(self):
        new_record = ("firulais", "10")
        insert_command = "INSERT INTO pet(name, age) VALUES('" + new_record[0] + "','" + new_record[1] + "')"
        pprint(insert_command)
        self.cursor.execute(insert_command)
    
    def query_all(self):
        self.cursor.execute("SELECT * FROM pet")
        cats = self.cursor.fetchall()
        for cat in cats:
            pprint("each pet : {0}".format(cat))
    
    def update_record(self):
        update_command = "UPDATE pet SET age=10 WHERE id=1"
        self.cursor.execute(update_command)

    def delete_record(self):
        delete_command = "DELETE from pet WHERE id=1"
        self.cursor.execute(delete_command)
    
    def drop_table(self):
        drop_table_command = "DROP TABLE pet"
        self.cursor.execute(drop_table_command)

if __name__ == '__main__':
    database_connection = DatabaseConnection()
    #database_connection.create_table()
    #database_connection.insert_new_record()
    #database_connection.update_record()
    database_connection.query_all()
    #database_connection.drop_table()
    #database_connection.delete_record()