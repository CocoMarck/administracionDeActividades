from .standard_table import StandardTable
from .tarea_table import TareaTable
from .recurso_table import RecursoHumanoTable
from .administrador_actividad import AdministracionDeActividad
from .database_names import RECURSOHUMANO_TABLE_NAMES, TAREA_TABLE_NAMES, ACTIVIDAD_TABLE_NAMES




class ActividadTable( StandardTable ):
    def __init__(self):
        super().__init__(
            database=AdministracionDeActividad(), table = ACTIVIDAD_TABLE_NAMES["table"]
        )
        self.column_soft_delete = ACTIVIDAD_TABLE_NAMES["low"]
        
        # Alias de Tablas
        self.ALIAS.update( 
            {
              "recursohumano" : "b",
              "tarea" : "c"
            }
        )
        
    def insert_actividad(
        self, TareaId: int, RecursoHumanoId: int, NOTA: str, FechaInicio: str, 
        FechaFin: str, HORAS: float, UsuarioCreacionId: int, FechaCreacion: str, UsuarioBajaId: int
    ) -> str | None:
        '''
        Se puede usar los modelos TareaTable y RecursoTable, para determinar si los Id elegidos existen y la fila a la que pertenecen, no esta en Baja
        '''
        sql_statement = (
            f"INSERT OR IGNORE INTO {self.table} ("
            f"{ACTIVIDAD_TABLE_NAMES['tareaid']}, {ACTIVIDAD_TABLE_NAMES['recursohumanoid']}, "
            f"{ACTIVIDAD_TABLE_NAMES['note']}, {ACTIVIDAD_TABLE_NAMES['startdate']}, "
            f"{ACTIVIDAD_TABLE_NAMES['enddate']}, {ACTIVIDAD_TABLE_NAMES['hours']}, "
            f"{ACTIVIDAD_TABLE_NAMES['usercreationid']}, " 
            f"{ACTIVIDAD_TABLE_NAMES['creationdate']}, {ACTIVIDAD_TABLE_NAMES['userlowid']}, "
            f"{ACTIVIDAD_TABLE_NAMES['low']} \n)\n"
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
            f"{ACTIVIDAD_TABLE_NAMES['tareaid']}={TareaId}, "
            f"{ACTIVIDAD_TABLE_NAMES['recursohumanoid']}={RecursoHumanoId}, "
            f"{ACTIVIDAD_TABLE_NAMES['note']}='{NOTA}', {ACTIVIDAD_TABLE_NAMES['startdate']}='{FechaInicio}', "
            f"{ACTIVIDAD_TABLE_NAMES['enddate']}='{FechaFin}', {ACTIVIDAD_TABLE_NAMES['hours']}={HORAS}, "
            f"{ACTIVIDAD_TABLE_NAMES['usermodificationid']}={UsuarioModificacionId}, "
            f"{ACTIVIDAD_TABLE_NAMES['modificationdate']}='{FechaModificacion}', "
            f"{ACTIVIDAD_TABLE_NAMES['userlowid']}={UsuarioBajaId}, "
            f"{ACTIVIDAD_TABLE_NAMES['lowdate']}='{FechaBaja}', {ACTIVIDAD_TABLE_NAMES['low']}={Baja}\n"
            f"WHERE {ACTIVIDAD_TABLE_NAMES['id']}={ActividadId};"
        )
        
        return self.database.execute_statement( sql_statement, commit=True, return_type="statement")
    
    
    
    def get_instruction_for_filetered_query(
        self, alias="", start_datetime: str=None, end_datetime: str=None, TareaId:int=None, RecursoHumanoId:int=None,
        Baja:int=0
    ):
        '''
        Obtener instruccion para una consulta filtrada
        '''
        alias = self.get_alias( alias, True )
            
        and_text = " AND "
        search_text = ""
        if isinstance(start_datetime, str) and isinstance(end_datetime, str):
            search_text += (
                f"{and_text}{alias}{ACTIVIDAD_TABLE_NAMES['startdate']} BETWEEN '{alias}{start_datetime}'"
                f"{and_text}'{alias}{end_datetime}'"
            )
    
        # Establecer parametros id's
        text_ids = ""
        if isinstance(TareaId, int):
            search_text += f"{and_text}{alias}{ACTIVIDAD_TABLE_NAMES['tareaid']}={TareaId} "

        if isinstance(RecursoHumanoId, int):
            search_text += f"{and_text}{alias}{ACTIVIDAD_TABLE_NAMES['recursohumanoid']}={RecursoHumanoId}"
        return search_text
    
    
    
    
    def filtered_query( 
        self, start_datetime: str=None, end_datetime: str=None, TareaId:int=None, RecursoHumanoId:int=None,
        Baja:int=0
    ):
        '''
        Obtiene datos de la tabla ACTIVIDAD, con filtros de: 
        TareaId, RecursoHumano, Baja=0, y eso basado en un rango de fechas.
        Esta metodo, actualmente jala medio raro, pero funciona
        '''
        search_text = self.get_instruction_for_filetered_query(
            "", start_datetime, end_datetime, TareaId, RecursoHumanoId, Baja
        )
        
        # Instrucción
        sql_statement = (
            f"SELECT * FROM {self.table} WHERE {self.column_soft_delete}={Baja} {search_text};"
        )
        
        #return sql_statement
        return self.database.execute_statement( sql_statement, commit=False, return_type="fetchall" )
        
        
        
    
    def get_columns_for_the_view(self):
        '''
        Obtener columnas para la vista. Solo info relevanta para el usuario final.
        '''
        keys = [
            'id', 'tareaid', 'description', 'recursohumanoid','name','note', 'startdate', 'enddate', 
            'hours', 'low'
        ]

        COLUMNS = {
            keys[0]: ACTIVIDAD_TABLE_NAMES[keys[0]],

            keys[1]: ACTIVIDAD_TABLE_NAMES[keys[1]],
            keys[2]: TAREA_TABLE_NAMES[keys[2]],

            keys[3]: ACTIVIDAD_TABLE_NAMES[keys[3]],
            keys[4]: RECURSOHUMANO_TABLE_NAMES[keys[4]],

            keys[5]: ACTIVIDAD_TABLE_NAMES[keys[5]],
            keys[6]: ACTIVIDAD_TABLE_NAMES[keys[6]],
            keys[7]: ACTIVIDAD_TABLE_NAMES[keys[7]],
            keys[8]: ACTIVIDAD_TABLE_NAMES[keys[8]],
            keys[9]: ACTIVIDAD_TABLE_NAMES[keys[9]],
        }
        return COLUMNS
    
    
    
    
    def get_instruction_for_the_view(self, Baja: int=None):
        '''
        Obtener instruccion para obtener los valores para la vista
        '''
        # Obtener columnas para la vista.
        COLUMNS = self.get_columns_for_the_view()
        
        # Para determinar baja o no
        text_where = "WHERE "
        if isinstance(Baja, int):
            text_where += f"{self.ALIAS['table']}.{COLUMNS['low']} = {Baja} AND {self.ALIAS['recursohumano']}.{RECURSOHUMANO_TABLE_NAMES['low']} = 0 AND "
            
        # Instruccion
        sql_statement = (
            f"SELECT {self.ALIAS['table']}.{COLUMNS['id']}, {self.ALIAS['table']}.{COLUMNS['tareaid']}, {self.ALIAS['tarea']}.{COLUMNS['description']}, " 
            f"{self.ALIAS['table']}.{COLUMNS['recursohumanoid']}, {self.ALIAS['recursohumano']}.{COLUMNS['name']}, "
            f"{self.ALIAS['table']}.{COLUMNS['note']}, {self.ALIAS['table']}.{COLUMNS['startdate']}, "
            f"{self.ALIAS['table']}.{COLUMNS['enddate']}, {self.ALIAS['table']}.{COLUMNS['hours']}, {self.ALIAS['table']}.{COLUMNS['low']}\n"
            f"  FROM {self.table} {self.ALIAS['table']}\n"

            f"INNER JOIN {RECURSOHUMANO_TABLE_NAMES['table']} {self.ALIAS['recursohumano']} on "
            f"{self.ALIAS['table']}.{ACTIVIDAD_TABLE_NAMES['recursohumanoid']} = {self.ALIAS['recursohumano']}.{RECURSOHUMANO_TABLE_NAMES['id']}\n"
            
            f"INNER JOIN {TAREA_TABLE_NAMES['table']} {self.ALIAS['tarea']} on "
            f"{self.ALIAS['table']}.{ACTIVIDAD_TABLE_NAMES['tareaid']} = {self.ALIAS['tarea']}.{TAREA_TABLE_NAMES['id']}\n"
            
            f"{text_where} {self.ALIAS['tarea']}.{RECURSOHUMANO_TABLE_NAMES['low']} = 0"
        )
        return sql_statement
    
    
    
    
    def get_values_for_the_view(self):
        '''
        Obtener una tabla así:
        0, 1, Texto, 0, Nombre, Texto, 0000-00-00, 0000-00-00, 0.0, False
        '''
        COLUMNS = self.get_columns_for_the_view()
        sql_statement = self.get_instruction_for_the_view() + ";"
        
        
        #return sql_statement
        return self.database.execute_statement( sql_statement, commit=False, return_type="fetchall" )
    
    
        
        
    def filtered_query_for_the_view( 
        self, start_datetime: str=None, end_datetime: str=None, TareaId:int=None, RecursoHumanoId:int=None,
        Baja:int=0
    ):
        '''
        Obtener datos filtrados para la vista
        Obtiene datos de la tabla ACTIVIDAD, con filtros de: 
        TareaId, RecursoHumano, Baja=0, y basado eso en un rango de fechas.
        Esta metodo, actualmente jala medio raro, pero funciona
        '''
        search_text = self.get_instruction_for_filetered_query(
            "table", start_datetime, end_datetime, TareaId, RecursoHumanoId, Baja
        )
        
        # Instrucción
        COLUMNS = self.get_columns_for_the_view()
        sql_statement = (
            f"{self.get_instruction_for_the_view(Baja=Baja)}"
            f"{search_text};"
        )
        
        return self.database.execute_statement( sql_statement, commit=False, return_type="fetchall" )
    
    
    def delete_actividad(self):
        pass