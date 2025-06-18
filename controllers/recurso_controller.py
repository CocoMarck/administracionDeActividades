import models
from .table_controller import TableController, get_datetime, text_or_none




class RecursoHumanoController( TableController ):
    def __init__(self, verbose: bool=True, return_message: bool=False, save_log: bool=True):
        super().__init__(
            table=models.RecursoHumanoTable(), verbose=verbose, return_message=return_message,
            save_log=save_log
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
                message = f"[SQL]\n{insert_user}"
                return_value = True
            else:
                message = f"[ERROR]\nBad instruction"
                return_value = False
        else:
            message = "[ERROR] Bad parameters"
            return_value = False
        
        return self.return_value( value=return_value, message=message )
    
    


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
                message = f"[INFO] Good instruction\n[SQL]\n{update}"
            else:
                message = f"[ERROR] Bad instruction\n[SQL]\n{update}"
        else:
            message = f"[ERROR] Bad parameters"
            value = False
        
        return self.return_value( value=value, message=message )
    



    def delete_user(self, RecursoHumanoId: int) -> bool | str:
        delete_user = self.table.delete_user( RecursoHumanoId )
        
        if isinstance( delete_user, str ):
            message = f"[SQL]\n{delete_user}"
            return_value = True
        else:
            message = f"[ERROR]\n{delete_user}"
            return_value = False
            
        return self.return_value( value=return_value, message=message )