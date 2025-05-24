import os, sys, sqlite3

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
        self, sql_statement: str, commit: bool = True, verbose: bool = False
    ) -> bool:
        '''
        Ejecutar alguna instrucción. 
        
        Returns:
            bool: Devuelve True si la instrucción se realizo correctamente, devuelve False si no pudo.
        '''
        # Mostrar instrucción en terminal
        if verbose:
            print( f'[SQL]\n{sql_statement}' )

        # Ejecutar instrucción
        try:
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute("BEGIN TRANSACTION") # Iniciar transacción Para que jale el rollback
                cursor.execute(sql_statement)

                if commit:
                    conn.commit()
                    if verbose:
                        print("[COMMIT] Changes made")
                else:
                    conn.rollback()
                    if verbose:                
                        print("[COMMIT] Discart changes")
            return True

        except sqlite3.OperationalError as e:
            print( f"[ERROR] {str(e)}" )
            return False
    

    def create_database(self, verbose: bool=False) -> bool:
        '''
        Crear base de datos vacia.
        
        Returns:
            bool: Si se crea la tabla True, de lo contrario False.
        '''
        if os.path.isfile(self.path_database):
            if verbose:
                print("[INFO] The database is already")
            return False
        else:
            try:
                conn = self.connect()
                conn.close()
                if verbose:
                    print("[SQL] Database created")
                return True
            except:
                if verbose:
                    print("[ERROR] The database could not be created" )
                return False
    
    
    def create_table_parameter( 
        self, table: str, sql_statement: str | list[ list[str] ], 
        commit: bool=False, verbose: bool=False
    ) -> bool:
        '''
        Para crear tablas. Depende de execute_statement.
        Solo poner statement de parametros para crear tablas. Se creara con un IF NOT EXISTS
        
        Returns:
            bool: True si la instucción esta buena, devuelve False si es mala
        '''
        parameter = ""
        if isinstance(sql_statement, str):
            # Solo es texto
            parameter = sql_statement
        elif isinstance(sql_statement, list):
            # Modo lista de string, o lista de lista de string
            for statement in sql_statement:
                parameter += "    "
                if isinstance(statement, str):
                    parameter += f"{statement}"
                if isinstance(statement, list):
                    for x in statement:
                        parameter += f"{x} "
                    parameter = parameter[:-1]
                parameter += ",\n"
            parameter = parameter[:-2]

        # Instrucción completa | Ejecución de instrucción
        full_sql_statement = (
            f"CREATE TABLE IF NOT EXISTS {table}(\n"
            f"{parameter}\n"
            f");"
        )
        return self.execute_statement( 
            sql_statement=full_sql_statement, commit=commit, verbose=verbose
        )
    
    
    def remove_table(self, table: str, commit: bool=False, varbose: bool=False):
        '''
        Remueva tabla. Depende de execute_statement
        '''
        pass