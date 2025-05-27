import sqlite3, os, sys
from .standard_database import StandardDataBase, struct_table_statement

class AdministracionDeActividad(StandardDataBase):
    def __init__(self, name_database="administracionDeActividad"):
    
        super().__init__( name_database=name_database, name_dir_data="data" )

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
                

    def create_table_instruction(self) -> list[str]:
        '''
        Lista de instrucciones para crear la tabla.
        '''
        list_instruction = []
        for key in self.dict_table.keys():
            full_sql_statement = struct_table_statement(
                type_statement = "create-table", table = key,
                sql_statement = self.dict_table[key]
            )
            list_instruction.append(full_sql_statement)
        return list_instruction
    
    
    def start_database(self) -> str | None:
        '''
        Crear base de datos
        
        Returns:
            str | None: 
                string si se creo la base de datos (texto de instrucciones).
                None si no se pudo crear la base de datos de manera correcta.
        '''
        create = self.create_database()
        
        text_instruction = ""
        for sql_statement in self.create_table_instruction():
            instruction = self.execute_statement( 
                sql_statement=sql_statement, commit=True, return_type="bool"
            )
            text_instruction += sql_statement + "\n"
        
        if create and instruction:
            return text_instruction[:-1]
        else:
            return None