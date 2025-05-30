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
    
    def insert_tarea(
        self, Descripcion: str, UsuarioCreacionId: int, FechaCreacion: str, 
        UsuarioModificacionId: int, FechaModificacion: str, UsuarioBajaId: int, FechaBaja: str, Baja: int
    ) -> str | None:
        sql_statement = (
            f"INSERT OR IGNORE INTO {self.table} (Descripcion, UsuarioCreacionId, "
            f"FechaCreacion, UsuarioModificacionId, FechaModificacion, UsuarioBajaId, FechaBaja, Baja)\n" 

            f"VALUES('{Descripcion}', {UsuarioCreacionId}, '{FechaCreacion}', "
            f"{UsuarioModificacionId}, '{FechaModificacion}', {UsuarioBajaId}, '{FechaBaja}', {Baja});"
        )
        
        return self.database.execute_statement( sql_statement, commit=True, return_type="statement" )
    
    
    def update_tarea(
        self, TareaId: int, Descripcion: str, UsuarioCreacionId: int, FechaCreacion: str, 
        UsuarioModificacionId: int, FechaModificacion: str, UsuarioBajaId: int, FechaBaja: str, Baja: int
    ):
        sql_statement = (
            f"UPDATE {self.table} SET "
            f"Descripcion='{Descripcion}', "
            f"UsuarioCreacionId={UsuarioCreacionId}, FechaCreacion='{FechaCreacion}', "
            f"UsuarioModificacionId={UsuarioModificacionId}, FechaModificacion='{FechaModificacion}', "
            f"UsuarioBajaId={UsuarioBajaId}, FechaBaja='{FechaBaja}', Baja={Baja}\n"
            
            f"WHERE TareaId={TareaId};"
        )

        return self.database.execute_statement( sql_statement, commit=True, return_type="statement" )
        #return sql_statement