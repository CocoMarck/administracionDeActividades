import sqlite3, os, sys
import models
from .database_controller import DataBaseController


class AdministracionDeActividadController( DataBaseController ):
    def __init__(self, verbose=True, return_message=False ):
        super().__init__( 
            database=models.AdministracionDeActividad(), 
            verbose=verbose, return_message=return_message
        )
    
    def start_database(self) -> bool | str:
        # Función
        start_database = self.database.start_database()
        
        if start_database != None:
            message = f"[SQL] Creating tables:\n{start_database}"
            return_value = True
        else:
            message = f"[ERROR] Bad statement"
            return_value = False
        
        if self.verbose: print(message)
        
        if self.return_message: 
            return message
        else:
            return return_value