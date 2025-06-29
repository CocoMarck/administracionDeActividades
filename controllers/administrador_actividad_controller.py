import sqlite3, os, sys
import models
from .database_controller import DatabaseController


class AdministracionDeActividadController( DatabaseController ):
    def __init__(self, verbose=True, return_message=False, log_level="warning", save_log: bool=True ):
        super().__init__( 
            database=models.AdministracionDeActividad(), 
            verbose=verbose, return_message=return_message, log_level=log_level, save_log=save_log
        )