import models
from .table_controller import TableController, get_datetime


class TareaController( TableController ):
    def __init__(self, verbose: bool=True, return_message: bool=False):
        super().__init__(
            table=models.TareaTable(), verbose=verbose, return_message=return_message
        )
    
    def insert_tarea(
        self, Descripcion: str
    ) -> bool | str:
        '''
        Establecer, descripcción, y fecha de creación, y su respectiva de Id
        '''
        # Función
        text = Descripcion
        return_value = False
        
        # Instrucción
        if Descripcion.replace(' ', '') != '':
            insert_tarea = self.table.insert_tarea( 
                Descripcion, 0, get_datetime(), 0
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
        '''
        Actualizar de TareaID; descripcción, y fecha de modificación, y su respectiva Id
        '''
        # Función
        text = Descripcion
        return_value = False

        # Valor de Baja correcto | Determinar fecha de baja o no
        if Baja < 0:
            Baja = 0
        if Baja > 1:
            Baja = 1

        time = get_datetime()
        if Baja == 1:   time_baja = time
        else:           time_baja = None
        
        # Determinar que los parametros sean correctos
        if Descripcion.replace(' ', '') == '':
            Descripcion = None
        
        # Establecer instrucción
        if TareaId > 0:
            update_tarea = self.table.update_tarea( 
                TareaId, Descripcion, 0, time, 0, time_baja, Baja
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