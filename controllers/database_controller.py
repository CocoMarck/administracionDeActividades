import models

class DataBaseController():
    def __init__(self, database: models.StandardDataBase, verbose=False):
        self.database = database
        self.verbose = verbose    
    
    def execute_statement(self, sql_statement: str, commit: bool = False) -> str:
        # Funcion
        execute = self.database.execute_statement( sql_statement, commit )
        
        # Mensaje
        message = f"[SQL] Statement:\n{sql_statement}"
        if execute:
            if commit:
                message += "\n[COMMIT] Changes made"
            else:
                message += "\n[COMMIT] Discart changes"
        else:
            message += f"\n[ERROR] bad sqlite statement"

        # Mostrar mensaje
        if self.verbose:
            print(message)
        
        # Devolver mensaje
        return message
    
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
        
        return message
    
    def delete_database(self) -> str:
        # Función
        delete = self.database.delete_database()
        
        if delete:
            message = "[SQL] Database deleted"
        else:
            message = "[WARNING] Database not deleted"
        
        if self.verbose:
            print(message)
        
        return message