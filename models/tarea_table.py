from .standard_table import StandardTable


class TareaTable(StandardTable):
    '''
    Manejar tabla TAREA de la base de datos administracionDeActividad
    '''
    def __init__(self):
        super().__init__(
            name_database="administracionDeActividad", name_dir_data="data", table="TAREA" 
        )