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
        SELECT t.TareaId, r.RecursoHumanoId
        FROM TAREA t
        JOIN RECURSO_HUMANO r
        WHERE t.TareaId = ? AND t.Baja = 0
          AND r.RecursoHumanoId = ? AND r.Baja = 0;
        
        
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
            


    def update_actividad(self):
        pass
    
    def delete_actividad(self):
        pass