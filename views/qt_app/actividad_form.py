from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import ( QTableWidget, QTableWidgetItem )
from views.interface.interface_number import *
from core.util_text import ignore_text_filter, pass_text_filter
from utils import ResourceLoader
import controllers




# Archivo ui
resource_loader = ResourceLoader()
dir_views = resource_loader.get_base_path( 'views' )
dir_ui = dir_views.joinpath( 'ui' )
file_ui = dir_ui.joinpath( 'actividad_form.ui' )


database_controller = controllers.AdministracionDeActividadController()
table_recurso = controllers.RecursoHumanoController( verbose=True, return_message=False )
table_tarea = controllers.TareaController( verbose=True, return_message=False )
table_actividad = controllers.ActividadController( verbose=True, return_message=False )
# Ventana
class ActividadForm(QtWidgets.QWidget):
    def __init__( self, table_controller=None ):
        super().__init__()

        self.resize( nums_win_main[0], nums_win_main[1] )
        uic.loadUi(file_ui, self)
        
        self.current_id = None
        
        self.table_controller = table_actividad
        
        self.button_add.clicked.connect( self.insert_actividad )
        
        self.refresh_table()
        self.refresh_combobox()
        

    def refresh_combobox(self):
        values = database_controller.execute_statement( 
            "SELECT * FROM TAREA WHERE Baja=0;", commit = False, return_type ="fetchall" 
        )
        print(values)
    
        self.combobox_tarea.clear()
        for value in table_tarea.get_all_value():
            if value[ len(value)-1 ] == 0: # Determinar baja
                self.combobox_tarea.insertItem( value[0], value[1] ) # id, descripcción
            
        self.combobox_recurso.clear()
        for value in table_recurso.get_all_value():
            if value[ len(value)-1 ] == 0: # Determinar baja
                self.combobox_recurso.insertItem( value[0], value[1] ) # id, descripcción
        

    def refresh_table(self):
        # Actualizar datos de la tabla.
        all_column = self.table_controller.get_all_column()
        self.table.clear()
        self.table.setColumnCount( len(all_column) )
        self.table.setHorizontalHeaderLabels( all_column )
        self.table.resizeColumnsToContents() # Para que se acomode por el texto columna.
        
        all_value = self.table_controller.get_all_value()
        self.table.setRowCount( len(all_value) )
        number = 0
        for column in all_column:
            for row in range(0, len(all_value)):
                final_text = str
                if number == 11:
                    pass
                    
                self.table.setItem( row, number, QTableWidgetItem( final_text ) )
                    
            number += 1
    

    def insert_actividad(self):
        print( self.combobox_tarea.currentIndex() )
        print( self.combobox_recurso.currentIndex() )
        print( self.time_hours.time() )