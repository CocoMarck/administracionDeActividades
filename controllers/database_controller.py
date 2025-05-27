import models

class DataBaseController():
    def __init__(self, database: models.StandardDataBase, verbose=False, return_message=False):
        self.database = database
        self.verbose = verbose
        self.return_message = return_message
    

    def execute_statement(
        self, sql_statement: str, commit: bool = False, return_type: str="cursor"
    ) -> str | bool | object | tuple | list:
        # Funcion
        execute = self.database.execute_statement( sql_statement, commit, return_type )
        
        # Mensaje
        message = f"[SQL] Statement:\n{sql_statement}"
        if execute != None:
            if commit:
                message += "\n[COMMIT] Changes made"
            else:
                message += "\n[COMMIT] Discart changes"
        else:
            message += f"\n[ERROR] bad sqlite statement"

        # Mostrar mensaje
        if self.verbose:
            print(message)
        
        # Devolver
        if self.return_message == True:
            return message
        else:
            return execute
    

    def create_database(self) -> str:
        # Funcion
        create = self.database.create_database()
        
        # Mensaje
        if create == "database-already" or create == "database-created":
            message = "[SQL] Database created"
        else:
            message = "[WARNING] The database could not be created"

        # Mostrar mensaje
        if self.verbose:
            print(message)
        
        # Devolver
        if self.return_message == True:
            return message
        else:
            return create
    

    def delete_database(self) -> str:
        # Función
        delete = self.database.delete_database()
        
        if delete:
            message = "[SQL] Database deleted"
        else:
            message = "[WARNING] Database not deleted"
        
        if self.verbose:
            print(message)
        
        # Devolver
        if self.return_message == True:
            return message
        else:
            return delete
    

    def tables(self) -> str | list:
        # Función
        tables = self.database.tables()
        
        return_tables = []
        message = ""
        if tables != None:
            message = (
                f"[SQL] Returning all tables\n"
                f"Tables: {tables}"
            )
            return_tables = tables
        else:
            message = "[WARNING] No detect tables"
        
        if self.verbose == True:
            print(message)
        
        # Devolver
        if self.return_message == True:
            return message
        else:
            return return_tables
    
    
    def exists_table(self, table: str) -> bool | str:
        # Función
        exists_table = self.database.exists_table( table=table )
        
        message = ""
        if exists_table:
            message = f'[SQL] The table "{table}" exists'
        else:
            message = f'[SQL] No exists the table "{table}"'
        
        if self.verbose:
            print(message)
        
        # Devolver
        if self.return_message:
            return message
        else:
            return exists_table
    
    
    def delete_table(self, table: str) -> bool | str:
        message = ""
    
        to_return = None
        delete = False
        if self.database.exists_table( table=table ):
            # Función
            delete = self.database.delete_table( table=table )
        
            if delete:
                message = f'[SQL] The table "{table}" was deleted'
            else:
                message = f'[SQL] The table "{table}" could not be deleted'
        else:
            message = f'[SQL] The table "{table}" does not exist and will not be deleted'
        
        if self.verbose:
            print(message)
        
        # Devolver
        if self.return_message:
            return message
        else:
            return delete
    
    
    def clear_database(self) -> bool | str:
        # Funcion
        clear = self.database.clear_database()
        
        if clear:   message = "[SQL] All tables were cleared"
        else:       message = "[SQL] There are no tables in the database"
        
        if self.verbose:    print(message)
        
        # Devolver
        if self.return_message: return message
        else:                   return clear