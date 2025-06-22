from .standard_table import StandardTable
from .administrador_actividad import AdministracionDeActividad
from .database_names import TAREA_TABLE_NAMES as TABLE_NAMES


class TareaTable(StandardTable):
    '''
    Manejar tabla TAREA de la base de datos administracionDeActividad
    '''
    def __init__(self):
        super().__init__(
            database=AdministracionDeActividad(), table=TABLE_NAMES["table"]
        )
        
        self.column_soft_delete = TABLE_NAMES["low"]
    

    def insert_tarea(
        self, Descripcion: str, UsuarioCreacionId: int, FechaCreacion: str, Baja: int
    ) -> str | None:
        '''
        Establecer, descripcción, y fecha de creación, y su respectiva de Id
        '''
        sql_statement = (
            f"INSERT OR IGNORE INTO {self.table} ({TABLE_NAMES['description']}, "
            f"{TABLE_NAMES['usercreationid']}, {TABLE_NAMES['creationdate']}, "
            f"{TABLE_NAMES['low']})\n" 

            f"VALUES('{Descripcion}', {UsuarioCreacionId}, '{FechaCreacion}', {Baja});"
        )
        
        return self.database.execute_statement( sql_statement, commit=True, return_type="statement" )
    
    
    def update_tarea(
        self, TareaId: int, Descripcion: str, UsuarioModificacionId: int, FechaModificacion: str, 
        UsuarioBajaId: int, FechaBaja: str, Baja: int
    ) -> str | None:
        '''
        Actualizar de TareaId; Descripcción, y Fecha de modificación, y su respectiva Id
        '''
        # Establecer o no parametros
        fecha_baja_text = f'{TABLE_NAMES["lowdate"]}='
        if FechaBaja == None:
            fecha_baja_text += 'null'
        else:
            fecha_baja_text += f"'{FechaBaja}'"
        
        if Descripcion == None:
            descripcion_text = ''
        else:
            descripcion_text = f"{TABLE_NAMES['description']}='{Descripcion}', "
            
        # Instrucción
        sql_statement = (
            f"UPDATE {self.table} SET "
            f"{descripcion_text}"
            f"{TABLE_NAMES['usermodificationid']}={UsuarioModificacionId}, "
            f"{TABLE_NAMES['modificationdate']}='{FechaModificacion}', "
            f"{TABLE_NAMES['userlowid']}={UsuarioBajaId}, "
            f"{fecha_baja_text}, {TABLE_NAMES['low']}={Baja}\n"
            
            f"WHERE {TABLE_NAMES['id']}={TareaId};"
        )

        return self.database.execute_statement( sql_statement, commit=True, return_type="statement" )