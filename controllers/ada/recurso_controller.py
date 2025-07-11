import models
from controllers.table_controller import TableController, get_datetime, text_or_none




class RecursoHumanoController( TableController ):
    def __init__(self, verbose: bool=True, log_level="warning", save_log: bool=True):
        super().__init__(
            table=models.RecursoHumanoTable(), verbose=verbose, log_level=log_level, save_log=save_log
        )
        

    def insert_user(
        self, Nombre: str, APP: str, APM: str, Puesto: str, 
    ) -> bool | str:
        if ( 
            isinstance( text_or_none(Nombre), str) and isinstance( text_or_none(APP), str) and 
            isinstance( text_or_none(APM), str) and isinstance( text_or_none(Puesto), str)
        ):
            insert_user = self.table.insert_user( 
                Nombre=Nombre, APP=APP, APM=APM, Puesto=Puesto, 
                UsuarioCreacionId=0, FechaCreacion=get_datetime()
            )
            if isinstance( insert_user, str ):
                message = f"\n{insert_user}"
                return_value = True
            else:
                message = "Bad instruction"
                return_value = False
        else:
            message = "Bad parameters"
            return_value = False
            
        if return_value == True:
            log_type = "info"
        else:
            log_type = "error"
        
        return self.return_value( value=return_value, message=message, log_type=log_type )
    
    


    def update_user(
        self, RecursoHumanoId: int, Nombre: str, APP: str, APM: str, Puesto: str, Baja: bool
    ) -> bool | str:
        value = False
        if (
            isinstance( RecursoHumanoId, int ) and isinstance( text_or_none(Nombre), str ) and
            isinstance( text_or_none(APP), str ) and isinstance( text_or_none(APM), str ) and
            isinstance( text_or_none(Nombre), str ) and isinstance(Baja, bool)
        ):
            update = self.table.update_user( 
                RecursoHumanoId=RecursoHumanoId, Nombre=Nombre, APP=APP, APM=APM, Puesto=Puesto, 
                UsuarioModificacionId=0, FechaModificacion=get_datetime(),
                UsuarioBajaId=0, FechaBaja=get_datetime(), Baja=int(Baja)
            )
            
            if isinstance( update, str ):
                value = True
                message = f"Good instruction\n[SQL]\n{update}"
            else:
                message = f"Bad instruction\n[SQL]\n{update}"
        else:
            message = f"Bad parameters"
            value = False
        
        if value:
            log_type = "info"
        else:
            log_type = "error"
        
        return self.return_value( value=value, message=message, log_type=log_type )
    



    def delete_user(self, RecursoHumanoId: int) -> bool | str:
        delete_user = self.table.delete_user( RecursoHumanoId )
        
        message = f"[SQL]\n{delete_user}"
        if isinstance( delete_user, str ):
            log_type = "info"
            return_value = True
        else:
            log_type = "error"
            return_value = False
            
        return self.return_value( value=return_value, message=message, log_type=log_type )