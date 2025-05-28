import models
from .table_controller import TableController


class TareaController( TableController ):
    def __init__(self, verbose: bool=True, return_message: bool=False):
        super().__init__(
            table=models.TareaTable(), verbose=verbose, return_message=return_message
        )
    
    def insert_tarea(
        self, TareaId, Descripcion, UsuarioCreacionId, FechaCreacion, UsuarioModificacionId,
        FechaModificacion, UsuarioBajaId, FechaBaja, Baja
    ):
        pass