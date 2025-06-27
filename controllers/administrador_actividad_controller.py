import sqlite3, os, sys
import models
from .database_controller import DatabaseController


class AdministracionDeActividadController( DatabaseController ):
    def __init__(self, verbose=True, return_message=False, save_log: bool=True ):
        super().__init__( 
            database=models.AdministracionDeActividad(), 
            verbose=verbose, return_message=return_message, save_log=save_log
        )
    
    def start_database(self) -> bool | str:
        # Función
        start_database = self.database.start_database()
        
        if start_database != None:
            log_type = "info"
            message = f"[SQL] Creating tables:\n{start_database}"
            return_value = True
        else:
            log_type = "error"
            message = f"Bad statement"
            return_value = False
        
        # Return
        return self.return_value( value=return_value, message=message, log_type=log_type )