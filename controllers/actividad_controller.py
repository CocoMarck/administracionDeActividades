import models
from .table_controller import TableController, get_datetime, text_or_none



class ActividadController( TableController ):
    def __init__( self, verbose: bool=True, return_message: bool=False ):
        super().__init__(
            table=models.ActividadTable(), verbose=verbose, return_message=return_message
        )
        self.tarea_table = models.TareaTable()
        self.recurso_table = models.RecursoHumanoTable()
        
    def insert_actividad(
        self, TareaId: int, RecursoHumanoId: int, NOTA: str, FechaInicio: str, 
        FechaFin: str, HORAS: str
    ) -> str | bool:
        
        # Determinar que existan los TareaId y RecursoHumnanoId
        exists_tarea_id = False
        tarea_values = self.tarea_table.get_all_values_without_soft_delete()
        for value in tarea_values:
            if TareaId == value[0]:
                exists_tarea_id = True
                break
                
        exists_recurso_id = False
        recurso_values = self.recurso_table.get_all_values_without_soft_delete()
        for value in recurso_values:
            if RecursoHumanoId == value[0]:
                exists_recurso_id = True
                break

        # Insertar o no
        if (
            isinstance(TareaId, int) and isinstance(RecursoHumanoId, int) and
            isinstance(text_or_none(NOTA), str) and isinstance(text_or_none(FechaInicio), str) and
            isinstance(text_or_none(FechaFin), str) and isinstance(text_or_none(HORAS), str) and
            (exists_tarea_id and exists_recurso_id)
        ):
            insert = self.table.insert_actividad(
                TareaId=TareaId, RecursoHumanoId=RecursoHumanoId, NOTA=NOTA, FechaInicio=FechaInicio, 
                FechaFin=FechaFin, HORAS=HORAS, UsuarioCreacionId=0, FechaCreacion=get_datetime(), 
                UsuarioBajaId=0
            )
        else:
            insert = None
        
        if isinstance(insert, str):
            message = f"[SQL]\n{insert}"
            return_value = True
        else:
            message = "[ERROR] Bad parameters"
            return_value = False
        
        if self.verbose:
            print(message)
        
        if self.return_message:
            return message
        else:
            return return_value