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
#table_actividad.delete_table()
# Ventana
class ActividadForm(QtWidgets.QWidget):
    def __init__( self, table_controller=None ):
        super().__init__()

        self.resize( nums_win_main[0], nums_win_main[1] )
        uic.loadUi(file_ui, self)
        
        self.current_id = None
        
        self.table_controller = table_actividad
        
        self.button_add.clicked.connect( self.insert_actividad )
        self.button_update.clicked.connect( self.update_actividad )
        
        self.refresh_text()
        self.refresh_table()
        self.refresh_combobox()
    
    

    def refresh_text(self):
        # Establecer texto
        self.label_id.setText( "ActividadId" )
        self.label_start_date.setText( "Fecha inicio" )
        self.label_end_date.setText( "Fecha fin" )
        self.label_note.setText( "Nota" )
        self.label_hours.setText( "Horas" )
        self.label_tarea.setText( "Tarea" )
        self.label_recurso.setText( "Recurso humano" )
        

    def refresh_combobox(self):
        # Establecer combobox
        self.combobox_tarea.clear()
        for value in table_tarea.get_all_values_without_soft_delete():
            self.combobox_tarea.addItem( value[1], userData=value[0] ) # descripcción, id
            
        self.combobox_recurso.clear()
        for value in table_recurso.get_all_values_without_soft_delete():
            self.combobox_recurso.addItem( value[1], userData=value[0] ) # descripcción, id
        

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
                if number == 13:
                    if all_value[row][number] == 1:
                        final_text = "Si"
                    else:
                        final_text = "No"
                else:
                    final_text = str(all_value[row][number])
                    
                self.table.setItem( row, number, QTableWidgetItem( final_text ) )
                    
            number += 1
    
    
    def dict_date_time(self):
        # Obtener parametros relacionados al tiempo
        time_qtime = self.time_hours.time()
        time_str = time_qtime.toString("HH:mm")
        
        start_qdate = self.start_date.date()
        start_date_str = str( start_qdate.toPyDate() )
        
        end_qdate = self.end_date.date()
        end_date_str = str( end_qdate.toPyDate() )

        dict_ready = {
            "start_date" : start_date_str,
            "end_date" : end_date_str,
            "hours" : time_str
        }
        
        return dict_ready
    

    def insert_actividad(self):
        # Insertar actividad
        date_time = self.dict_date_time()

        table_actividad.insert_actividad(
            TareaId=self.combobox_tarea.currentData(), 
            RecursoHumanoId=self.combobox_recurso.currentData(),
            NOTA=self.entry_note.text(), FechaInicio=date_time["start_date"], FechaFin=date_time["end_date"],
            HORAS=date_time["hours"]
        )
        self.refresh_table()
    

    def update_actividad(self):
        # Actualizar actividad
        date_time = self.dict_date_time()
        
        table_actividad.update_actividad(
            ActividadId=1, 
            TareaId=self.combobox_tarea.currentData(), 
            RecursoHumanoId=self.combobox_recurso.currentData(), 
            NOTA=self.entry_note.text(), FechaInicio=date_time["start_date"], 
            FechaFin=date_time["end_date"], HORAS=date_time["hours"], UsuarioId=0, Baja=1
        )
        self.refresh_table()