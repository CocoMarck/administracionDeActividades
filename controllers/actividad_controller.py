import models
from .table_controller import TableController, get_datetime, text_or_none



class ActividadController( TableController ):
    def __init__( self, verbose: bool=True, return_message: bool=False, save_log: bool=True ):
        super().__init__(
            table=models.ActividadTable(), verbose=verbose, return_message=return_message,
            save_log=save_log
        )
        self.tarea_table = models.TareaTable()
        self.recurso_table = models.RecursoHumanoTable()
    


    def exists_tarea_id( self, tarea_id:int ):
        # Determinar que existe TareaId
        exists_tarea_id = False
        tarea_values = self.tarea_table.get_all_values_without_soft_delete()
        for value in tarea_values:
            if tarea_id == value[0]:
                exists_tarea_id = True
                break
        return exists_tarea_id
        
    
    def exists_recurso_id( self, recurso_id:int ):
        # Determinar que existe RecursoHumnanoId
        exists_recurso_id = False
        recurso_values = self.recurso_table.get_all_values_without_soft_delete()
        for value in recurso_values:
            if recurso_id == value[0]:
                exists_recurso_id = True
                break
        return exists_recurso_id
        

    def insert_actividad(
        self, TareaId: int, RecursoHumanoId: int, NOTA: str, FechaInicio: str, 
        FechaFin: str, HORAS: str
    ) -> str | bool:
        # Determinar que existen Id's
        exists_tarea_id = self.exists_tarea_id( TareaId )
        exists_recurso_id = self.exists_recurso_id( RecursoHumanoId )

        # Insertar o no
        if (
            isinstance(TareaId, int) and isinstance(RecursoHumanoId, int) and
            isinstance(text_or_none(NOTA), str) and isinstance(text_or_none(FechaInicio), str) and
            isinstance(text_or_none(FechaFin), str) and isinstance( HORAS, float) and
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
            log_type = "info"
            message = f"[SQL]\n{insert}"
            return_value = True
        else:
            log_type = "error"
            message = "Bad parameters"
            return_value = False
        
        # return
        return self.return_value( value=return_value, message=message, log_type=log_type )
    
    
    
    def update_actividad(
        self, ActividadId: int, TareaId: int, RecursoHumanoId: int, NOTA: str, FechaInicio: str, 
        FechaFin: str, HORAS: float, UsuarioId:int=0, Baja: int=0
    ):
        message = ""
    
        # Determinar que existen Id's
        exists_tarea_id = self.exists_tarea_id( TareaId )
        exists_recurso_id = self.exists_recurso_id( RecursoHumanoId )
        
        if exists_tarea_id and exists_recurso_id:
            exists_ids = True
            message += "The id's exits"
        else:
            exists_ids = False
            message += "Not exists de id's"
        
        # Determinar que baja es correcto.
        if Baja == 1 or Baja == 0:
            good_soft_delete = True
            FechaBaja = get_datetime()
            message += "\nGood soft delete parameter"
        else:
            good_soft_delete = False
            FechaBaja = None
            message += "\nBad soft delete parameter"

        # Determinar que los parametros son correctos
        if (
            isinstance(ActividadId, int) and exists_ids and isinstance( text_or_none(NOTA), str) and 
            isinstance( text_or_none(FechaInicio), str) and isinstance( text_or_none(FechaFin), str) and 
            isinstance( HORAS, float ) and isinstance(UsuarioId, int) and good_soft_delete
        ):
            update = self.table.update_actividad(
                ActividadId=ActividadId, TareaId=TareaId, RecursoHumanoId=RecursoHumanoId, 
                NOTA=NOTA, FechaInicio=FechaInicio, FechaFin=FechaFin, HORAS=HORAS,
                UsuarioModificacionId=UsuarioId, FechaModificacion=get_datetime(), 
                UsuarioBajaId=UsuarioId, FechaBaja=FechaBaja, Baja=Baja
            )
        else:
            update = None
            
        if isinstance(update, str):
            log_type = "info"
            message += f"\n[SQL]\n{update}"
            return_value = True
        else:
            log_type = "error"
            message += f"\nBad parameters"
            return_value = False
        
        # return
        return self.return_value( value=return_value, message=message, log_type=log_type )
    
    
    
    
    def filtered_query(
        self, start_datetime: str=None, end_datetime: str=None, TareaId:int=None, RecursoHumanoId:int=None,
        Baja: bool=False
    ):
        '''
        Permite hacer una consulta de datos filtrados. Los parametros son los filtros.
        '''
        value = []
    
        # Determinar que la baja sea un boleano
        if isinstance( Baja, bool):
            # Establecer lista de valores.
            filtered_query = self.table.filtered_query(
                start_datetime=start_datetime, end_datetime=end_datetime,
                TareaId=TareaId, RecursoHumanoId=RecursoHumanoId, Baja=int(Baja)
            )
            if isinstance(filtered_query, list):
                log_type = "info"
                message = f"Range of datetime; {start_datetime} to {end_datetime}"
                value = filtered_query
            else:
                log_type = "error"
                message = (
                    f"Bad parameters: `start = {start_datetime}` `end = {end_datetime}` "
                    f"`tarea id = {TareaId}` `recurso humano id = {RecursoHumanoId}`"
                )
        else:
            log_type = "error"
            message = "Bad `Baja` parameter"
        

        return self.return_value( value=value, message=message, log_type=log_type )