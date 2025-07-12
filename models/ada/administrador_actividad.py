import sqlite3, os, sys
from models.standard_database import StandardDatabase, struct_table_statement
from models.model_names.ada_names import (
    TABLE_CONTROL_FIELDS, ADA_DATABASE_NAMES, TAREA_TABLE_NAMES, RECURSOHUMANO_TABLE_NAMES,
    ACTIVIDAD_TABLE_NAMES
)

class AdministracionDeActividad(StandardDatabase):
    def __init__(self, name_database=ADA_DATABASE_NAMES["name"] ):
    
        super().__init__( name_database=name_database, name_dir_data="data" )

        # Datos de columnas/campos a crear
        '''
        sqlite3 no tiene tipos de datos bool, ni bit. El intiger 0/1, se usa como los bool. Se puede asignar a los integer las palabras TRUE y FALSE. Se puede declarar como tipo INTEGER
        No existe TEXT, se usa TEXT en su lugar. Con estructura ISO8601 ("YYYY-MM-DD HH:MM:SS.SSS")
        '''
        self.control_fields = [
            [ TABLE_CONTROL_FIELDS["usercreationid"], "INTEGER", "NULL" ],
            [ TABLE_CONTROL_FIELDS["creationdate"], "TEXT", "NULL" ],
            [ TABLE_CONTROL_FIELDS["usermodificationid"], "INTEGER", "NULL" ],
            [ TABLE_CONTROL_FIELDS["modificationdate"], "TEXT", "NULL" ],
            [ TABLE_CONTROL_FIELDS["userlowid"], "INTEGER", "NULL" ],
            [ TABLE_CONTROL_FIELDS["lowdate"], "TEXT", "NULL" ],
            [ TABLE_CONTROL_FIELDS["low"], "INTEGER", "DEFAULT 0" ]
        ]

        self.dictionary_of_tables = {
            TAREA_TABLE_NAMES["table"]: [
                [ TAREA_TABLE_NAMES["id"], "INTEGER", "PRIMARY KEY AUTOINCREMENT" ],
                [ TAREA_TABLE_NAMES["description"], "VARCHAR", "NULL" ]
            ],
            RECURSOHUMANO_TABLE_NAMES["table"]: [
                [ RECURSOHUMANO_TABLE_NAMES["id"], "INTEGER", "PRIMARY KEY AUTOINCREMENT" ],
                [ RECURSOHUMANO_TABLE_NAMES["name"], "VARCHAR(40)", "NULL" ],
                [ RECURSOHUMANO_TABLE_NAMES["paternal_surname"], "VARCHAR(40)", "NULL" ],
                [ RECURSOHUMANO_TABLE_NAMES["maternal_surname"], "VARCHAR(40)", "NULL" ],
                [ RECURSOHUMANO_TABLE_NAMES["position"], "VARCHAR(40)", "NULL" ]
            ],
            ACTIVIDAD_TABLE_NAMES["table"]: [
                [ ACTIVIDAD_TABLE_NAMES["id"], "INTEGER", "PRIMARY KEY AUTOINCREMENT" ],
                [ ACTIVIDAD_TABLE_NAMES["tareaid"], "INTEGER", "NOT NULL" ],

                [ ACTIVIDAD_TABLE_NAMES["recursohumanoid"], "INTEGER", "NOT NULL" ],
                [ ACTIVIDAD_TABLE_NAMES["note"], "TEXT", "NULL" ],
                [ ACTIVIDAD_TABLE_NAMES["startdate"], "TEXT", "NOT NULL" ],
                [ ACTIVIDAD_TABLE_NAMES["enddate"], "TEXT", "NOT NULL" ],
                [ ACTIVIDAD_TABLE_NAMES["hours"], "DECIMAL", "NOT NULL" ],
            ]
        }

        for key in self.dictionary_of_tables.keys():
            for field in self.control_fields:
                self.dictionary_of_tables[ key ].append(field)
        
        # El FOREIGN KEY va al ultimo.
        for x in [
            [ 
                f"FOREIGN KEY ({ACTIVIDAD_TABLE_NAMES['tareaid']}) REFERENCES "
                f"{TAREA_TABLE_NAMES['table']}({TAREA_TABLE_NAMES['id']})" 
            ],
            [ 
                f"FOREIGN KEY ({ACTIVIDAD_TABLE_NAMES['recursohumanoid']}) REFERENCES "
                f"{RECURSOHUMANO_TABLE_NAMES['table']}({RECURSOHUMANO_TABLE_NAMES['id']})" 
            ]
        ]:
            self.dictionary_of_tables[ ACTIVIDAD_TABLE_NAMES["table"] ].append(x)
        
        # Para que jale el `foreign_keys`
        self.additional_instructions_for_tables = [
            "PRAGMA foreign_keys = ON;"
        ]