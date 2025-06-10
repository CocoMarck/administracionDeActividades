from .standard_table import StandardTable
from .administrador_actividad import AdministracionDeActividad




class ActividadTable( StandardTable ):
    def __init__(self):
        super().__init__(
            database=AdministracionDeActividad(), table = "ACTIVIDAD"
        )
        
    def insert_actividad(self):
        pass

    def update_actividad(self):
        pass
    
    def delete_actividad(self):
        pass