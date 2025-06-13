from views.interface.interface_number import *
from core.util_text import ignore_text_filter, pass_text_filter
from utils import ResourceLoader
from controllers.table_controller import get_datetime
import controllers

from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import ( QTableWidget, QTableWidgetItem )
from PyQt6.QtCore import QDate, QTime




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
        self.entry_id.textChanged.connect( self.on_text_changed )
        
        self.refresh_text()
        self.refresh_table()
        self.refresh_combobox()
        self.refresh_date()

        
    def on_text_changed(self, text):
        # Solo aceptar numeros en el entry
        self.entry_id.setText( ignore_text_filter(text, "1234567890")  )
        
        # Determinar que se escribio un id
        self.entry_note.setText( "" )
        self.checkbox_soft_delete.setChecked( False )
        if self.entry_id.text() != '':
            self.current_id = int(self.entry_id.text()) 

            # Establecer descripcción y baja por medio del id
            for column in table_actividad.get_all_value():
                if self.current_id == column[0]:
                    self.entry_note.setText( column[3] )

                    # Combos
                    tarea_index = self.combobox_tarea.findData( column[1] )
                    self.combobox_tarea.setCurrentIndex( tarea_index )
                    
                    recurso_index = self.combobox_recurso.findData( column[2] )
                    self.combobox_recurso.setCurrentIndex( recurso_index )
                    
                    # Dates
                    qdate_start = QDate.fromString( str(column[4]), "yyyy-MM-dd" )
                    self.start_date.setDate( qdate_start )
                    
                    qdate_end = QDate.fromString( column[5], "yyyy-MM-dd" )
                    self.end_date.setDate( qdate_end )
                    
                    # Hora
                    qtime = QTime.fromString( column[6], "hh:mm" )
                    self.time_hours.setTime(qtime)
                    print(column[6])

                    # Checkbox
                    self.checkbox_soft_delete.setChecked( bool(column[13]) )
                    break
        else:
            self.current_id = None
    

    def refresh_text(self):
        # Establecer texto
        self.label_id.setText( "ActividadId" )
        self.label_start_date.setText( "Fecha inicio" )
        self.label_end_date.setText( "Fecha fin" )
        self.label_note.setText( "Nota" )
        self.label_hours.setText( "Horas" )
        self.label_tarea.setText( "Tarea" )
        self.label_recurso.setText( "Recurso humano" )
        
        
    def refresh_date(self):
        date_str = get_datetime( "date" )
        qdate = QDate.fromString( date_str, "yyyy-MM-dd" )
        self.start_date.setDate(qdate)
        self.end_date.setDate(qdate)
        

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
            ActividadId=self.current_id, 
            TareaId=self.combobox_tarea.currentData(), 
            RecursoHumanoId=self.combobox_recurso.currentData(), 
            NOTA=self.entry_note.text(), FechaInicio=date_time["start_date"], 
            FechaFin=date_time["end_date"], HORAS=date_time["hours"], UsuarioId=0, 
            Baja=int(self.checkbox_soft_delete.isChecked())
        )
        self.refresh_table()