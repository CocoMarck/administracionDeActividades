import models


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