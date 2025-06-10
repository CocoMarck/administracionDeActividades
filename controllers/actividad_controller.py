import models
from .table_controller import TableController, get_datetime, text_or_none



class ActividadController( TableController ):
    def __init__( self, verbose: bool=True, return_message: bool=False ):
        super().__init__(
            table=models.ActividadTable(), verbose=verbose, return_message=return_message
        )