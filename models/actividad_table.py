from .standard_table import StandardTable
from .tarea_table import TareaTable
from .recurso_table import RecursoHumanoTable
from .administrador_actividad import AdministracionDeActividad




class ActividadTable( StandardTable ):
    def __init__(self):
        super().__init__(
            database=AdministracionDeActividad(), table = "ACTIVIDAD"
        )
        self.column_soft_delete = "Baja"
        
    def insert_actividad(
        self, TareaId: int, RecursoHumanoId: int, NOTA: str, FechaInicio: str, 
        FechaFin: str, HORAS: float, UsuarioCreacionId: int, FechaCreacion: str, UsuarioBajaId: int
    ) -> str | None:
        '''
        Se puede usar los modelos TareaTable y RecursoTable, para determinar si los Id elegidos existen y la fila a la que pertenecen, no esta en Baja.
        '''
        sql_statement = (
            f"INSERT OR IGNORE INTO {self.table} ("
            f"TareaId, RecursoHumanoId, NOTA, FechaInicio, FechaFin, HORAS, UsuarioCreacionId, " 
            f"FechaCreacion, UsuarioBajaId, Baja"
            f")\n"
            f"VALUES ({TareaId}, {RecursoHumanoId}, '{NOTA}', '{FechaInicio}', '{FechaFin}', {HORAS}, "
            f"{UsuarioCreacionId}, '{FechaCreacion}', {UsuarioBajaId}, 0);"
        )
        return self.database.execute_statement( sql_statement, commit=True, return_type="statement")
            


    def update_actividad(
        self, ActividadId: int, TareaId: int, RecursoHumanoId: int, NOTA: str, FechaInicio: str, 
        FechaFin: str, HORAS: float, UsuarioModificacionId: int,
        FechaModificacion: str, UsuarioBajaId: int, FechaBaja: str, Baja: int
    ):
        sql_statement = (
            f"UPDATE {self.table} SET "
            f"TareaId={TareaId}, RecursoHumanoId={RecursoHumanoId}, NOTA='{NOTA}', FechaInicio='{FechaInicio}', "
            f"FechaFin='{FechaFin}', HORAS={HORAS}, UsuarioModificacionId={UsuarioModificacionId}, "
            f"FechaModificacion='{FechaModificacion}', UsuarioBajaId={UsuarioBajaId}, FechaBaja='{FechaBaja}', "
            f"Baja={Baja}\n"
            f"WHERE ActividadId={ActividadId};"
        )
        
        return self.database.execute_statement( sql_statement, commit=True, return_type="statement")
    
    
    def filtered_query( 
        self, start_datetime: str=None, end_datetime: str=None, TareaId:int=None, RecursoHumanoId:int=None,
        Baja:int=0
    ):
        '''
        Obtiene datos de la tabla ACTIVIDAD, con filtros de: 
        TareaId, RecursoHumano, Baja=0, y eso basado en un rango de fechas.
        Esta metodo, actualmente jala medio raro, pero funciona.
        '''
        search_text = ""
        if isinstance(start_datetime, str) and isinstance(end_datetime, str):
            search_text += f"FechaInicio BETWEEN '{start_datetime}' AND '{end_datetime}'"
    
        # Establecer parametros id's
        text_ids = ""
        
        if search_text != "":
            and_text = " AND "
        else:
            and_text = ""
        
        if isinstance(TareaId, int):
            search_text += f"{and_text}TareaId={TareaId} "
            
        if search_text != "":
            and_text = " AND "
        else:
            and_text = ""

        if isinstance(RecursoHumanoId, int):
            search_text += f"{and_text}RecursoHumanoId={RecursoHumanoId}"
        
        # Establecer texto de baja
        if search_text != "":
            search_text += " AND "
        
        # Instrucción
        sql_statement = (
            f"SELECT * FROM {self.table} WHERE {search_text}{self.column_soft_delete}={Baja};"
        )
        
        #return sql_statement
        return self.database.execute_statement( sql_statement, commit=False, return_type="fetchall" )
    
    
    def delete_actividad(self):
        pass