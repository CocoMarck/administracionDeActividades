import models
import datetime



def get_datetime():
    return str( datetime.datetime.now().replace(microsecond=0).isoformat() )
    
    
def text_or_none( text: str ):
    # Determinar que el texto no este vacio "". Si lo esta, devuelve None, y si no el text/string.
    if bool( text.strip() ) == True:
        return text
    else:
        return None




class TableController():
    def __init__( self, table: models.StandardTable, verbose: bool=True, return_message: bool=False ):
        self.table = table
        self.name = table.table
        self.verbose = verbose
        self.return_message = return_message
        
    def get_all_column(self):
        '''
        Mostrar todas las columnas de la tabla.
        '''
        all_column = self.table.get_all_column( )
        return_value = []
        if all_column == [] or all_column == None:
            message = f"[INFO] {self.name}: Not have columns"
        else:
            message = f"[INFO] {self.name}: Have columns:\n{all_column}"
            return_value = all_column
        
        if self.verbose:
            print( message )

        if self.return_message:
            return_value = message

        return return_value
    
    def get_all_value(self):
        '''
        Mostrar todas los valores de la tabla.
        '''
        all_value = self.table.get_all_value( )
        return_value = []
        if all_value == [] or all_value == None:
            message = f"[INFO] {self.name}: Not have values"
        else:
            message = f"[INFO] {self.name}: Have values:\n{all_value}"
            return_value = all_value
        
        if self.verbose:
            print( message )

        if self.return_message:
            return_value = message

        return return_value
        

    def clear_table(self) -> str | bool:
        clear_table = self.table.clear_table()
        if clear_table != None:
            message = f'[SQL]\n{clear_table}\n[INFO] The table {self.name} was clear'
            return_value = True
        else:
            message = f'[ERROR] {self.name}'
            return_value = False
        
        if self.verbose: print(message)
        
        if self.return_message: return_value = message
        
        return return_value
        


    def delete_row_by_column_value(self, column: str, value: str) -> str | bool:
        delete_value = self.table.delete_row_by_column_value( column, value )
        
        if isinstance( delete_value, str ):
            message = f'[SQL]\n{delete_value}'
            return_value = True
        else:
            message = f'[ERROR] {self.name}'
            return_value = False
        
        if self.return_message: return_value = message

        if self.verbose: print(message)
        
        return return_value