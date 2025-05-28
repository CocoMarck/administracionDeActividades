from .standard_database import StandardDataBase, struct_table_statement


class StandardTable():
    '''
    Para manejar una tabla de una base de datos.
    No crea tablas, no crea la base de datos. No tiene funcion para ejecutar sql statements
    Usa un StandartDataBase, para manejar una tabla. Solo una tabla.
    '''
    def __init__(
        self, name_database=str, name_dir_data: str="data", table=str
    ):
        self.database = StandardDataBase( name_database, name_dir_data )
        self.table = table

    def get_all_column(self):
        '''
        Mostrar todas las columnas de la tabla.
        '''
        return self.database.get_table_all_column( table=self.table )
    
    def get_all_value(self):
        '''
        Mostrar todas los valores de la tabla.
        '''
        return self.database.get_table_all_value( table=self.table )
        
    def get_type_parameter(self):
        '''
        sqlite3 Obtener tipo de dato de las columnas de la tabla
        '''
        pass