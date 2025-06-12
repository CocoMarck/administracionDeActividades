from .standard_table import StandardTable
from .administrador_actividad import AdministracionDeActividad


class RecursoHumanoTable( StandardTable ):
    '''
    Manejar tabla RECURSO_HUMANO de la base de datos administracionDeActividad
    '''
    def __init__(self):
        super().__init__(
            database=AdministracionDeActividad(), table="RECURSO_HUMANO"
        )
        self.column_soft_delete = "Baja"
        
    def insert_user(
        self, Nombre: str, APP: str, APM: str, Puesto: str, 
        UsuarioCreacionId: int, FechaCreacion: str
    ):
        sql_statement = (
            f"INSERT OR IGNORE INTO {self.table} "
            f"(Nombre, APP, APM, Puesto, UsuarioCreacionId, FechaCreacion)\n"
            f"VALUES( '{Nombre}', '{APP}', '{APM}', '{Puesto}', {UsuarioCreacionId}, '{FechaCreacion}' );"
        )
        
        return self.database.execute_statement( sql_statement, commit=True, return_type="statement" )
    
    
    def update_user(
        self, RecursoHumanoId: int, Nombre: str, APP: str, APM: str, Puesto: str, 
        UsuarioModificacionId: int, FechaModificacion: str,
        UsuarioBajaId: int, FechaBaja: str, Baja: int
    ):
        sql_statement = (
            f"UPDATE {self.table} SET Nombre='{Nombre}', APP='{APP}', APM='{APM}', Puesto='{Puesto}', "
            f"UsuarioModificacionId={UsuarioModificacionId}, FechaModificacion='{FechaModificacion}', "
            f"UsuarioBajaId={UsuarioBajaId}, FechaBaja='{FechaBaja}', Baja={Baja}\n"
            f"WHERE RecursoHumanoId={RecursoHumanoId};"
        )
        
        return self.database.execute_statement( sql_statement, commit=True, return_type="statement" )
    

    def delete_user(self, RecursoHumanoId: int) -> str | None:
        return self.delete_row_by_column_value(
            column = "RecursoHumanoId", value = f"{RecursoHumanoId}"
        )