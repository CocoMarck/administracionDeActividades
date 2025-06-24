import models
import datetime
from .logging_controller import LoggingController



def get_datetime( mode: str="dateTime") -> str:
    dateTime = str( datetime.datetime.now().replace(microsecond=0).isoformat() )
    if mode == "date" or mode == "time":
        time_or_date = dateTime.split("T")
        
        if mode == "date":
            return time_or_date[0]
        elif mode == "time":
            return time_or_date[1]
    else:
        return dateTime
    
    
def text_or_none( text: str ) -> str | None:
    # Determinar que el texto no este vacio "". Si lo esta, devuelve None, y si no el text/string.
    if bool( text.strip() ) == True:
        return text
    else:
        return None




class TableController( LoggingController ):
    def __init__( 
        self, table: models.StandardTable, verbose: bool=True, return_message: bool=False,
        log_level: str="warning", save_log: bool=True
    ):
        self.table = table
        self.name = table.table
        
        # Log
        super().__init__( 
            name=f"table_{self.name.lower()}", verbose=verbose, return_message=return_message,
            log_level=log_level, save_log=save_log
        )
    
        
    def get_all_columns(self):
        '''
        Mostrar todas las columnas de la tabla.
        '''
        all_column = self.table.get_all_columns( )
        return_value = []
        if all_column == [] or all_column == None:
            message = f"{self.name}: Not have columns"
        else:
            message = f"{self.name}: Have columns:\n{all_column}"
            return_value = all_column

        return self.return_value( value=return_value, message=message, log_type="info" )
    

    def get_all_values(self):
        '''
        Mostrar todas los valores de la tabla.
        '''
        all_value = self.table.get_all_values( )
        return_value = []
        if all_value == [] or all_value == None:
            message = f"{self.name}: Not have values"
        else:
            message = f"{self.name}: Have values:\n{all_value}"
            return_value = all_value
        
        return self.return_value( value=return_value, message=message, log_type="info" )
        

    def get_all_values_without_soft_delete(self) -> str | None:
        '''
        Mostrar todos los valores sin baja
        '''
        all_value = self.table.get_all_values_without_soft_delete()
        return_value = []
        if all_value == [] or all_value == None:
            message = f"{self.name}: Not have values"
        else:
            message = f"{self.name}: Have values without soft delete:\n{all_value}"
            return_value = all_value
        
        return self.return_value( value=return_value, message=message, log_type="info" )
        

    def clear_table(self) -> str | bool:
        clear_table = self.table.clear_table()
        if clear_table != None:
            log_type = "info"
            message = f'[SQL]\n{clear_table}\nThe table {self.name} was clear'
            return_value = True
        else:
            log_type = "error"
            message = f'{self.name}'
            return_value = False
        
        return self.return_value( value=return_value, message=message, log_type=log_type )
        
        
        
    def delete_table(self) -> str | bool:
        delete_table = self.table.delete_table()
        if delete_table != None:
            log_type = "info"
            message = f'[SQL]\n{delete_table}\nThe table {self.name} was deleted'
            return_value = True
        else:
            log_type = "error"
            message = f'{self.name}'
            return_value = False
            
        return self.return_value( value=return_value, message=message, log_type=log_type )
        


    def delete_row_by_column_value(self, column: str, value: str) -> str | bool:
        delete_value = self.table.delete_row_by_column_value( column, value )
        
        if isinstance( delete_value, str ):
            log_type = "info"
            message = f'[SQL]\n{delete_value}'
            return_value = True
        else:
            log_type = "error"
            message = f'{self.name}'
            return_value = False
        
        return self.return_value( value=return_value, message=message, log_type=log_type )