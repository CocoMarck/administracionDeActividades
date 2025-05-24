import sqlite3, os, sys

class AdministracionDeActividad():
    def __init__(self, name_db = "administracionDeActividad"):
        # Ruta
        current_dir = os.path.dirname( os.path.abspath(sys.argv[0]) )
        self.dir_data = os.path.join( current_dir, 'data' )

        # Archivo de base de datos
        self.name_db = name_db
        db_format = ".db"
        self.db_file_name = f'{self.name_db}{db_format}'
        self.file_db = os.path.join( self.dir_data, self.db_file_name)

        # Datos de columnas/campos a crear
        '''
        sqlite3 no tiene tipos de datos bool, ni bit. El intiger 0/1, se usa como los bool. Se puede asignar a los integer las palabras TRUE y FALSE. Se puede declarar como tipo INTEGER
        No existe TEXT, se usa TEXT en su lugar. Con estructura ISO8601 ("YYYY-MM-DD HH:MM:SS.SSS")
        '''
        self.control_fields = [
            [ "UsuarioCreacionId", "INTEGER", "NULL" ],
            [ "FechaCreacion", "TEXT", "NULL" ],
            [ "UsuarioModificacionId", "INTEGER", "NULL" ],
            [ "FechaModificacion", "TEXT", "NULL" ],
            [ "UsuarioBajaId", "INTEGER", "NULL" ],
            [ "FechaBaja", "TEXT", "NULL" ],
            [ "Baja", "INTEGER", "DEFAULT 0" ]
        ]

        self.dict_table = {
            "TAREA": [
                [ "TareaId", "INTEGER", "PRIMARY KEY AUTOINCREMENT" ],
                [ "Decripcion", "VARCHAR", "NULL" ]
            ],
            "RECURSO_HUMANO": [
                [ "RecursoHumanoId", "INTEGER", "PRIMARY KEY AUTOINCREMENT" ],
                [ "Nombre", "VARCHAR(40)", "NULL" ],
                [ "APP", "VARCHAR(40)", "NULL" ],
                [ "APM", "VARCHAR(40)", "NULL" ],
                [ "Puesto", "VARCHAR(40)", "NULL" ]
            ],
            "ACTIVIDAD": [
                [ "ActividadId", "INTEGER", "PRIMARY KEY AUTOINCREMENT" ],
                [ "TareaId", "INTEGER", "NOT NULL" ],
                [ "NOTA", "TEXT", "NULL" ],
                [ "FechaInicio", "TEXT", "NOT NULL" ],
                [ "FechaFin", "TEXT", "NOT NULL" ],
                [ "HORAS", "DECIMAL", "NOT NULL" ]
            ]
        }

        for key in self.dict_table.keys():
            for field in self.control_fields:
                self.dict_table[ key ].append(field)

    def connect(self):
        return sqlite3.connect( self.db_file )
    
    def all_sql_statement(self):
        '''
        Devolver la instrucciónes para crear db, con todos sus tablitas
        '''
        # Intrucción de creación de tabla
        all_sql_statement = []
        for table in self.dict_table.keys():
            fields = ''

            for column in self.dict_table[table]:
                fields += "    "
                for param in column:
                    fields += f'{param} '
                fields = fields[:-1]
                fields += ",\n"
            fields = fields[:-2]
                    
            sql_statement = (
            f"CREATE TABLE IF NOT EXISTS {table} (\n"
            f"{fields}\n"
            f");"
            )
            all_sql_statement.append( sql_statement )

        return all_sql_statement
        

    def create_db(self):
        # Ejecutar instruccion
        for sql_statement in self.all_sql_statement():
            print(sql_statement)
            #with self.connect() as conn:
            #    conn.execute(sql_statement)
            #    conn.commit()