import models
from .table_controller import TableController, get_datetime, text_or_none



class ActividadController( TableController ):
    def __init__( self, verbose: bool=True, return_message: bool=False ):
        super().__init__(
            table=models.ActividadTable(), verbose=verbose, return_message=return_message
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
        
        # Mostrar
        if self.verbose:
            print(message)
        
        # Devolver
        if self.return_message:
            return message
        else:
            return return_value
    
    
    
    def update_actividad(
        self, ActividadId: int, TareaId: int, RecursoHumanoId: int, NOTA: str, FechaInicio: str, 
        FechaFin: str, HORAS: str, UsuarioId: int, Baja: int
    ):
        message = ""
    
        # Determinar que existen Id's
        exists_tarea_id = self.exists_tarea_id( TareaId )
        exists_recurso_id = self.exists_recurso_id( RecursoHumanoId )
        
        if exists_tarea_id and exists_recurso_id:
            exists_ids = True
            message += "[INFO] The id's exits"
        else:
            exists_ids = False
            message += "[ERROR] Not exists de id's"
        
        # Determinar que baja es correcto.
        if Baja == 1 or Baja == 0:
            good_soft_delete = True
            FechaBaja = get_datetime()
            message += "\n[INFO] Good soft delete parameter"
        else:
            good_soft_delete = False
            FechaBaja = None
            message += "\n[ERROR] Bad soft delete parameter"

        # Determinar que los parametros son correctos
        if (
            isinstance(ActividadId, int) and exists_ids and isinstance(NOTA, str) and 
            isinstance(FechaInicio, str) and isinstance(FechaFin, str) and isinstance(HORAS, str) and 
            isinstance(UsuarioId, int) and good_soft_delete
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
            message += f"\n[SQL]\n{update}"
            return_value = True
        else:
            message += f"\n[ERROR] Bad parameters"
            return_value = False
        
        # Mostrar
        if self.verbose:
            print(message)
        
        # Devolver
        if self.return_message:
            return message
        else:
            return return_value