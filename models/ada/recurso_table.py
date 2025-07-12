from models.standard_table import StandardTable
from .administrador_actividad import AdministracionDeActividad
from models.model_names.ada_names import RECURSOHUMANO_TABLE_NAMES as TABLE_NAMES


class RecursoHumanoTable( StandardTable ):
    '''
    Manejar tabla RECURSO_HUMANO de la base de datos administracionDeActividad
    '''
    def __init__(self):
        super().__init__(
            database=AdministracionDeActividad(), table=TABLE_NAMES['table']
        )
        self.column_soft_delete = TABLE_NAMES['low']
        
        # Columnas para la vista
        keys_for_the_view = ['id', 'name', 'paternal_surname', 'maternal_surname', 'position', 'low']
        self.COLUMNS_FOR_THE_VIEW = {}
        for key in keys_for_the_view:
            self.COLUMNS_FOR_THE_VIEW.update( {key: TABLE_NAMES[key]} )
        

    def insert_user(
        self, Nombre: str, APP: str, APM: str, Puesto: str, 
        UsuarioCreacionId: int, FechaCreacion: str
    ):
        sql_statement = (
            f"INSERT OR IGNORE INTO {self.table} "
            f"({TABLE_NAMES['name']}, {TABLE_NAMES['paternal_surname']}, "
            f"{TABLE_NAMES['maternal_surname']}, {TABLE_NAMES['position']}, "
            f"{TABLE_NAMES['usercreationid']}, {TABLE_NAMES['creationdate']})\n"
            f"VALUES( '{Nombre}', '{APP}', '{APM}', '{Puesto}', {UsuarioCreacionId}, '{FechaCreacion}' );"
        )
        
        return self.database.execute_statement( sql_statement, commit=True, return_type="statement" )
    
    
    def update_user(
        self, RecursoHumanoId: int, Nombre: str, APP: str, APM: str, Puesto: str, 
        UsuarioModificacionId: int, FechaModificacion: str,
        UsuarioBajaId: int, FechaBaja: str, Baja: int
    ):
        sql_statement = (
            f"UPDATE {self.table} SET {TABLE_NAMES['name']}='{Nombre}', "
            f"{TABLE_NAMES['paternal_surname']}='{APP}', {TABLE_NAMES['maternal_surname']}='{APM}', "
            f"{TABLE_NAMES['position']}='{Puesto}', "
            f"{TABLE_NAMES['usermodificationid']}={UsuarioModificacionId}, "
            f"{TABLE_NAMES['modificationdate']}='{FechaModificacion}', "
            f"{TABLE_NAMES['userlowid']}={UsuarioBajaId}, {TABLE_NAMES['lowdate']}='{FechaBaja}', "
            f"{TABLE_NAMES['low']}={Baja}\n"
            f"WHERE {TABLE_NAMES['id']}={RecursoHumanoId};"
        )
        
        return self.database.execute_statement( sql_statement, commit=True, return_type="statement" )
    

    def delete_user(self, RecursoHumanoId: int) -> str | None:
        return self.delete_row_by_column_value(
            column = TABLE_NAMES['id'], value = f"{RecursoHumanoId}"
        )