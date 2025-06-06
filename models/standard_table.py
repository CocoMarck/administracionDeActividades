from .standard_database import StandardDataBase, struct_table_statement


class StandardTable():
    '''
    Para manejar una tabla de una base de datos.
    No crea tablas, no crea la base de datos. No tiene funcion para ejecutar sql statements
    Usa un StandartDataBase, para manejar una tabla. Solo una tabla.
    '''
    def __init__(
        self, database: StandardDataBase, table=str
    ):
        self.database = database
        self.table = table

    def get_all_column(self):
        '''
        Mostrar todas las columnas de la tabla.
        '''
        return self.database.get_table_all_column( table=self.table )
    
    def get_all_value(self):
        '''
        Mostrar todas los valores de la tabla.
        '''
        return self.database.get_table_all_value( table=self.table )
        
    def get_type_parameter(self):
        '''
        sqlite3 Obtener tipo de dato de las columnas de la tabla
        '''
        pass
    
    def clear_table(self) -> str | None:
        '''
        sqlite3 Eliminar todos las filas de la tabla.
        
        DELETE FROM table;

        Para eliminar secuencia autoincrement de tabla (si es que tiene)
        DELETE FROM sqlite_sequence WHERE name='tabla';
        '''
        
        # Instrucciones SQLite
        sqlite_sequence = self.database.execute_statement( 
            f"DELETE FROM sqlite_sequence WHERE name='{self.table}';", commit=True, return_type="statement"
        )
        clear_table = self.database.execute_statement( 
            f'DELETE FROM "{self.table}";', commit=True, return_type="statement"
        )
        
        # Determinar qeue devolver
        sql_statement = ""
        return_string = False

        if isinstance(clear_table, str):
            sql_statement += f"{clear_table} "
        if isinstance(sqlite_sequence, str):
            sql_statement += sqlite_sequence
        if isinstance(clear_table, str) or isinstance(sqlite_sequence, str):
            return_string = True
        
        # Devovler valor, ya sea None o str
        if return_string == True:
            return sql_statement
        else:
            return None
    

    def delete_table(self):
        pass
    
    
    def delete_row_by_column_value(self, column: str, value: str) -> str | None:
        '''
        Eliminar una fila por el valor de una columna. Normalmente el Id.
        '''
        sql_statement = struct_table_statement( 
            type_statement="delete-value", table=self.table, sql_statement=[ column, value ]
        )
        
        # Ejecutar instrucción
        delete_value = self.database.execute_statement( 
            sql_statement, commit=True, return_type="statement"
        )
        return delete_value