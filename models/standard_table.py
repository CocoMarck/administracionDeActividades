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
        self.column_soft_delete = "softDelete"

    def get_all_column(self) -> list:
        '''
        Mostrar todas las columnas de la tabla.
        '''
        return self.database.get_table_all_column( table=self.table )
    
    def get_all_value(self) -> list:
        '''
        Mostrar todas los valores de la tabla.
        '''
        return self.database.get_table_all_value( table=self.table )
        
    def get_all_values_without_soft_delete(self) -> str | None:
        '''
        Obtener datos sin baja
        '''
        sql_statement = (
            f"SELECT * FROM {self.table} WHERE {self.column_soft_delete}=0;"
        )
        return self.database.execute_statement( sql_statement, commit=False, return_type="fetchall" )
        
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
    

    def delete_table(self) -> str | None:
        full_sql_statement = self.clear_table()
        if full_sql_statement == None:
            full_sql_statement = ""
        
        sql_statement = self.database.delete_table( self.table )
        if sql_statement == True:
            full_sql_statement += f"\nDROP {self.table};"
        
        if full_sql_statement == "":
            full_sql_statement = None
        
        return full_sql_statement
    
    
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