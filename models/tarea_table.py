from .standard_table import StandardTable
from .administrador_actividad import AdministracionDeActividad


class TareaTable(StandardTable):
    '''
    Manejar tabla TAREA de la base de datos administracionDeActividad
    '''
    def __init__(self):
        super().__init__(
            database=AdministracionDeActividad(), table="TAREA" 
        )
        
        #print( self.database.dict_table[ self.table ] )
        #print( self.get_all_column() )
    
    def insert_tarea(
        self, Descripcion: str, UsuarioCreacionId: int, FechaCreacion: str, Baja: int
    ) -> str | None:
        '''
        Establecer, descripcción, y fecha de creación, y su respectiva de Id
        '''
        sql_statement = (
            f"INSERT OR IGNORE INTO {self.table} (Descripcion, UsuarioCreacionId, FechaCreacion, Baja)\n" 

            f"VALUES('{Descripcion}', {UsuarioCreacionId}, '{FechaCreacion}', {Baja});"
        )
        
        return self.database.execute_statement( sql_statement, commit=True, return_type="statement" )
    
    
    def update_tarea(
        self, TareaId: int, Descripcion: str, UsuarioModificacionId: int, FechaModificacion: str, 
        UsuarioBajaId: int, FechaBaja: str, Baja: int
    ):
        '''
        Actualizar de TareaID; descripcción, y fecha de modificación, y su respectiva Id
        '''
        # Establecer o no parametros
        fecha_baja_text = 'FechaBaja='
        if FechaBaja == None:
            fecha_baja_text += 'null'
        else:
            fecha_baja_text += f"'{FechaBaja}'"
        
        if Descripcion == None:
            descripcion_text = ''
        else:
            descripcion_text = f"Descripcion='{Descripcion}', "
            
        # Instrucción
        sql_statement = (
            f"UPDATE {self.table} SET "
            f"{descripcion_text}"
            f"UsuarioModificacionId={UsuarioModificacionId}, FechaModificacion='{FechaModificacion}', "
            f"UsuarioBajaId={UsuarioBajaId}, {fecha_baja_text}, Baja={Baja}\n"
            
            f"WHERE TareaId={TareaId};"
        )

        return self.database.execute_statement( sql_statement, commit=True, return_type="statement" )
        #return sql_statement