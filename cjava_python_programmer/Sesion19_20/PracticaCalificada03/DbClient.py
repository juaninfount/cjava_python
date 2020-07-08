import psycopg2
from Alumno import Alumno
from pprint import pprint

class DbClient:

    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                "dbname='bd_colegio' user='postgres' host='localhost' password='postgresql' port='5432'  "
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            pprint("Conexion exitosa")
            self._create_table()
        except:
            pprint("No se pudo conectar a la base de datos")

    def _create_table(self):
        sql_command = """ 
                        CREATE TABLE ALUMNO(
                            ID  SERIAL PRIMARY KEY,
                            CODIGO char(6) not null,
                            NOMBRE varchar(100),
                            APELLIDO_PAT varchar(100),
                            APELLIDO_MAT varchar(100), 
                            CELULAR varchar(10)
                        );
                      """
        pprint(sql_command)
        self.cursor.execute(sql_command)        
        
    def _insert_new_record(self, alumno):         
        sql_command = """INSERT INTO ALUMNO(codigo, nombre, apellido_pat, apellido_mat, celular)
                        VALUES('%s','%s','%s','%s','%s') """ % ( alumno.codigo, alumno.nombre, alumno.apellido_pat, alumno.apellido_mat, alumno.celular)

        pprint(sql_command)
        self.cursor.execute(sql_command)
        return 1

    def _update_record(self, alumno):
        sql_command = """ UPDATE ALUMNO SET nombre='%s', apellido_pat='%s', apellido_mat='%s', celular='%s'
                           WHERE id in (SELECT a.id from ALUMNO a where a.codigo = '%s') """ % ( alumno.nombre, alumno.apellido_pat, alumno.apellido_mat, alumno.celular, alumno.codigo)
        pprint(sql_command)
        self.cursor.execute(sql_command)
        return 1

    def _delete_record(self, codigo):
        sql_command = """ delete from ALUMNO WHERE codigo = '%s' """ % ( codigo )
        pprint(sql_command)
        self.cursor.execute(sql_command)
        return 1

    def _select_record(self, codigo):
        sql_command = """ SELECT codigo, nombre, apellido_pat, apellido_mat, celular FROM ALUMNO WHERE ID in 
                       (SELECT a.id from ALUMNO a where a.codigo = '%s') """ % (codigo)
        pprint(sql_command)        
        self.cursor.execute(sql_command)

        alumnos = []

        rows = self.cursor.fetchall()        
        for row in rows:
            alumnos.append(Alumno(row[0],row[1],row[2],row[3],row[4]))
            
        return alumnos
    
    def ingresar_registros_alumno(self):
        
        alumno = Alumno('001','JUAN ANTONIO','PEREZ','CASTRO','943345671')
        self._insert_new_record(alumno)

        alumno = Alumno('002','LESLIE MARGOT','TRIGOSO','SANTOS','934145673')
        self._insert_new_record(alumno)

        alumno = Alumno('003','TERESA LEONA','DAMARIZ','TENORIO','944567133')
        self._insert_new_record(alumno)

    def modificar_registro(self, alumno):                
        self._update_record(alumno)

    def eliminar_registro(self, codigo):
        self._delete_record('002')

    def lectura_registro(self, codigo):
        alumnos = self._select_record(codigo)

        pprint(""" Alumno -->
                    Codigo: %s,
                    Nombre: %s,
                    Apellido Paterno: %s,
                    Apellido Materno: %s,
                    Celular: : %s
                """ % (alumnos[0].codigo, alumnos[0].nombre, alumnos[0].apellido_pat, alumnos[0].apellido_mat, alumnos[0].celular ) )
        
if __name__ == "__main__":
    dbclient = DbClient()
    dbclient.ingresar_registros_alumno()
    dbclient.modificar_registro(Alumno('003','LUIS ANTONIO','SAMIR','DOMINGUEZ', '932234561'))
    dbclient.eliminar_registro('002')
    dbclient.lectura_registro('001')
