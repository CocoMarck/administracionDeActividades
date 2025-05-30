import models
from .table_controller import TableController


class TareaController( TableController ):
    def __init__(self, verbose: bool=True, return_message: bool=False):
        super().__init__(
            table=models.TareaTable(), verbose=verbose, return_message=return_message
        )
    
    def insert_tarea(
        self, Descripcion: str
    ) -> bool | str:
        # Función
        text = Descripcion
        return_value = False
        if Descripcion.replace(' ', '') != '':
            insert_tarea = self.table.insert_tarea( 
                Descripcion, 1, "00-00-00", 1, "00-00-00", 1, "00-00-00", 0 
            )
            
            if insert_tarea != None:
                message = f'[SQL]\n{insert_tarea}'
                return_value = True
            else:
                message = '[ERROR] Bad statement'
        
        else:
            message = "[ERROR] Bad description"
        
        # Verbose Mesasge
        if self.verbose:
            print(message)

        # Return
        if self.return_message:
            return message
        else:
            return return_value
            
            
            
            
    def update_tarea(
        self, TareaId: int, Descripcion: str, Baja: int
    ) -> bool | str:
        # Función
        text = Descripcion
        return_value = False

        if Baja < 0:
            Baja = 0
        if Baja > 1:
            Baja = 1

        if Descripcion.replace(' ', '') != '' and TareaId > 0:
            update_tarea = self.table.update_tarea( 
                TareaId, Descripcion, 1, "00-00-00", 1, "00-00-00", 1, "00-00-00", Baja
            )
            
            if update_tarea != None:
                message = f'[SQL]\n{update_tarea}'
                return_value = True
            else:
                message = '[ERROR] Bad statement'
        
        else:
            message = "[ERROR] Bad description"
        
        # Verbose Mesasge
        if self.verbose:
            print(message)

        # Return
        if self.return_message:
            return message
        else:
            return return_value