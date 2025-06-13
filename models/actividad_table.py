from .standard_table import StandardTable
from .tarea_table import TareaTable
from .recurso_table import RecursoHumanoTable
from .administrador_actividad import AdministracionDeActividad




class ActividadTable( StandardTable ):
    def __init__(self):
        super().__init__(
            database=AdministracionDeActividad(), table = "ACTIVIDAD"
        )
        
    def insert_actividad(
        self, TareaId: int, RecursoHumanoId: int, NOTA: str, FechaInicio: str, 
        FechaFin: str, HORAS: str, UsuarioCreacionId: int, FechaCreacion: str, UsuarioBajaId: int
    ) -> str | None:
        '''
        Se puede usar los modelos TareaTable y RecursoTable, para determinar si los Id elegidos existen y la fila a la que pertenecen, no esta en Baja.
        '''
        sql_statement = (
            f"INSERT OR IGNORE INTO {self.table} ("
            f"TareaId, RecursoHumanoId, NOTA, FechaInicio, FechaFin, HORAS, UsuarioCreacionId, " 
            f"FechaCreacion, UsuarioBajaId, Baja"
            f")\n"
            f"VALUES ({TareaId}, {RecursoHumanoId}, '{NOTA}', '{FechaInicio}', '{FechaFin}', '{HORAS}', "
            f"{UsuarioCreacionId}, '{FechaCreacion}', {UsuarioBajaId}, 0);"
        )
        return self.database.execute_statement( sql_statement, commit=True, return_type="statement")
            


    def update_actividad(
        self, ActividadId: int, TareaId: int, RecursoHumanoId: int, NOTA: str, FechaInicio: str, 
        FechaFin: str, HORAS: str, UsuarioModificacionId: int,
        FechaModificacion: str, UsuarioBajaId: int, FechaBaja: str, Baja: int
    ):
        sql_statement = (
            f"UPDATE {self.table} SET "
            f"TareaId={TareaId}, RecursoHumanoId={RecursoHumanoId}, NOTA='{NOTA}', FechaInicio='{FechaInicio}', "
            f"FechaFin='{FechaFin}', HORAS='{HORAS}', UsuarioModificacionId={UsuarioModificacionId}, "
            f"FechaModificacion='{FechaModificacion}', UsuarioBajaId={UsuarioBajaId}, FechaBaja='{FechaBaja}', "
            f"Baja={Baja}\n"
            f"WHERE ActividadId={ActividadId};"
        )
        
        return self.database.execute_statement( sql_statement, commit=True, return_type="statement")
    
    
    def delete_actividad(self):
        pass