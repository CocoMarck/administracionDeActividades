import os, sys, sqlite3




def detect_list_datatype( variable: str | list | list[str], datatype=str):
    '''
    Detecta lista de tipo de dato:
    datatype, list[datatype], list[ list[datatype] ]
    Returns:
        None, datatype, list[datatype], list[ list[datatype] ]
    '''
    # datatype
    if isinstance(variable, datatype):
        return datatype
    elif isinstance(variable, list):
        # list[datatype]
        if all(isinstance(value, datatype) for value in variable):
            return list[datatype]

        # list[ list[datatype] ]
        elif all(isinstance(value, list) for value in variable):
            if all(isinstance(value_value, datatype) for value in variable for value_value in value):
                return list[list[datatype]]
    # None
    return None

def from_list_to_string( variable: list, space="" ):
    data_type = detect_list_datatype( variable, str )

    final_text = ""
    
    # El string
    if data_type == str:
        final_text = variable

    elif data_type == list[str]:
        # Modo lista de string
        final_text += space
        for text in variable:
            final_text += f"{text}, "
        final_text = final_text[:-2]

    elif data_type == list[list[str]]:
        # Lista de lista de string
        for text in variable:
            final_text += space
            for x in text:
                final_text += f"{x} "
            final_text = final_text[:-1]
            final_text += ",\n"
        final_text = final_text[:-2]
    
    return final_text
    
    
    

    
    
def struct_table_statement( 
    type_statement: str, table: str=str, 
    sql_statement: str | list[str] | list[list[str]] = str
) -> str:
    '''
    Estructurar una Declaración para sqlite3 dependiendo de los parametros.
    
    Args:
        type_statement: str: Tipo de instrucción, opciones:
            create-table, para crear una tabla.
            select-column, para seleccionar una columna
            insert-or-update, para insertar dato o actualizar dato en tabla.
            delete-value, para borrar un valor en una tabla (columna/valor).
        table: str.
            Nombre de la tabla.
        sql_statement: str | list[str] | list[list[str]]
            datos para estructurar en la declaración.
    
    Returns:
        string: Declaración para sqlite3
    '''
    # Inicailizar
    type_statement = type_statement.lower().replace( " ", "")
    full_sql_statement = ""
    
    go = False
    if type_statement == "tables" or type_statement == "delete-table":
        # Forzar statement
        go = True
    else:
        # Determinar tipo de dato            
        data_type = detect_list_datatype(sql_statement, str)
        
        # Establecer o no statement
        go = (data_type != None) and isinstance(table, str)
    
    # Opciones
    space = "    "
    if go:
        if type_statement=='create-table':
            parameter = from_list_to_string( sql_statement, space=space )
                
            # Instrucción completa | Ejecución de instrucción
            full_sql_statement = (
                f"CREATE TABLE IF NOT EXISTS {table}(\n"
                f"{parameter}\n"
                f");"
            )
        elif type_statement=='select-column':
            if data_type == list[str]:
                column = from_list_to_string( sql_statement )
            else:
                column = sql_statement

            full_sql_statement = (
                f'SELECT {column} FROM {table};'
            )

        elif type_statement=='insert-or-update' and data_type == list[str]:
            column = sql_statement[0]
            value = sql_statement[1]
            conflict = sql_statement[2]
            
            full_sql_statement = (
                f"INSERT OR IGNORE INTO {table} ({column})\n"
                f"VALUES({value})\n"
                f"ON CONFLICT({conflict}) DO UPDATE SET {column}={value};"
            )
        elif type_statement=="delete-value" and data_type == list[str]:
            column = sql_statement[0]
            value = sql_statement[1]
            full_sql_statement = (
                f'DELETE FROM {table}\n'
                f'WHERE {column} = {value};'
            )
        
        # Los que solo necesitan "type_statement"
        elif type_statement=="delete-table":
            full_sql_statement = f"DROP TABLE IF EXISTS {table};"
        
        elif type_statement=="tables":
            full_sql_statement = "SELECT name FROM sqlite_master WHERE type='table';"
        

    return full_sql_statement




class StandardDataBase():
    '''
    Un objeto modelo estandar para manejar una base de datos sqlite3
    '''
    def __init__(self, name_database, name_dir_data="data"  ):
        # Ruta
        self.dir_current = os.path.dirname( os.path.abspath(sys.argv[0]) )
        self.name_dir_data = name_dir_data
        self.name_database = name_database
        
        # Ruta | Declarar dir_data y path_database
        self.set_directory_data()
        self.set_database_path()
    

    def set_directory_data(self) -> None:
        '''
        Función necesaria para declarar el atrubuto: dir_data
        '''
        self.dir_data = os.path.join( self.dir_current, self.name_dir_data )
    
    
    def set_database_path(self) -> None:
        '''
        Función necesaria para declarar el atrubuto: path_database
        '''
        self.path_database = os.path.join( self.dir_data, f'{self.name_database}.db' )
    
    
    def connect(self) -> sqlite3.Connection:
        '''
        Conectar con db y devolver la coneccion
        '''
        return sqlite3.connect( self.path_database )
    
    
    def execute_statement(
        self, sql_statement: str, commit: bool = True, return_type: str = "cursor"
    ) -> None | tuple | list | object:
        '''
        Ejecutar alguna instrucción. 
        
        Returns:
            list | tuple | None | cursor: 
            Devuelve algo si la instrucción se realizo correctamente (Por defecto un objeto cursor).
            Devuelve None si no pudo.
        '''
        # Ejecutar instrucción
        try:
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute("BEGIN TRANSACTION") # Iniciar transacción Para que jale el rollback
                cursor.execute(sql_statement)

                if commit:
                    conn.commit()
                else:
                    conn.rollback()

                if return_type == "cursor":
                    return cursor
                elif return_type == "fetchall":
                    return cursor.fetchall()
                elif return_type == "fetchone":
                    return cursor.fetchone()
                elif return_type == "statement":
                    return sql_statement
                else:
                    return True

        #except sqlite3.OperationalError as e:
        except Exception as e:
            return None
    

    def create_database(self) -> str | None:
        '''
        Crear base de datos vacia.
        
        Returns:
            bool: Si se crea la tabla True, de lo contrario False.
        '''
        message = None
        if os.path.isfile(self.path_database):
            message = "database-already"
        else:
            try:
                message = "database-created"
                conn = self.connect()
                conn.close()
            except:
                pass
        return message
                
                
    def delete_database(self) -> bool:
        '''
        Remueve base de datos
        '''
        if os.path.isfile( self.path_database ):
            os.remove( self.path_database )
        
        return not os.path.isfile( self.path_database )
    

    def tables(self) -> list | None:
        '''
        Detecta todas las tablas disponibles
        
        Returns:
            list | None: Lista de tablas que tiene la base de datos. O none si no se pudo.
        '''
        fetchall_tables = self.execute_statement( 
            sql_statement=struct_table_statement( "tables" ), 
            commit=False, return_type="fetchall" 
        )
        tables = []
        if fetchall_tables != None:
            for name in fetchall_tables:
                tables.append( name[0] )
            return tables
        else: return None
        
    

    def exists_table(self, table: str) -> bool:
        '''
        Detecta si existe una tabla
        
        Returns:
            bool: True si existe, False si no existe.
        '''
        all_tables = self.tables()
        exists = False
        if all_tables != None:
            for table_name in all_tables:
                if table == table_name:
                    exists = True
                    break
        return exists
    

    def delete_table(self, table: str) -> bool:
        '''
        Borra una tabla existente.

        Returns:
            bool: True si borra tabla o no existe tabla, False si existe pero no puede borrar tabla.
        '''
        sql_statement = struct_table_statement( "delete-table", table )
        return ( self.execute_statement(sql_statement, commit=True, return_type="bool") != None )
    

    def clear_database(self) -> bool:
        '''
        Borra todas las tablas
        
        Returns:
            bool: True borra todas las tablas. Lo contrario es un false.
        '''
        all_tables = self.tables()
        if all_tables != None:
            # Aca pasa el False
            all_deleted = True
            for table_name in all_tables:
                if self.delete_table( table=table_name ) == False: 
                    all_deleted = False
            return all_deleted
        else:
            return True
    

    def get_table_all_column(self, table: str) -> list | None:
        #sql_statement = f"SELECT * FROM {table};"
        sql_statement = struct_table_statement( "select-column", table, "*" )
        cursor = self.execute_statement( sql_statement, commit=False, return_type="cursor" )

        if cursor != None:
            # Establecer lista, y deveolver lista
            return_list = []
            for x in cursor.description:
                return_list.append( x[0] )
        
            return return_list
        else:
            return None
    
    
    def get_table_all_value(self, table: str) -> list | None:
        sql_statement = struct_table_statement( "select-column", table, "*" )
        #sql_statement = struct_table_statement( 
        #    "select-column", table, self.get_table_all_column( table=table )
        #)
        return self.execute_statement( sql_statement=sql_statement, commit=False, return_type="fetchall" )