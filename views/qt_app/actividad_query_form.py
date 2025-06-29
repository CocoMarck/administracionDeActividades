from views.interface.interface_number import *
from core.text_util import ignore_text_filter, pass_text_filter
from core.time_util import (
    get_datetime, get_first_day_of_the_month, get_end_day_of_the_month,
    get_date_from_formatted_datetime, get_time_from_formatted_datetime
)
from utils import ResourceLoader

from models.database_names import RECURSOHUMANO_TABLE_NAMES, TAREA_TABLE_NAMES, ACTIVIDAD_TABLE_NAMES
import controllers

from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import ( QTableWidget, QTableWidgetItem )
from PyQt6.QtCore import QDate, QDateTime, QTime




# Archivo ui
resource_loader = ResourceLoader()
dir_views = resource_loader.get_base_path( 'views' )
dir_ui = dir_views.joinpath( 'ui' )
file_ui = dir_ui.joinpath( 'actividad_query_form.ui' )




# Controlador
database_controller = controllers.AdministracionDeActividadController()
actividad_controller = controllers.ActividadController()
tarea_controller = controllers.TareaController()
recurso_controller = controllers.RecursoHumanoController()




class ActividadQueryForm(QtWidgets.QWidget):
    def __init__( self ):
        super().__init__()

        self.resize( nums_win_main[0], nums_win_main[1] )
        uic.loadUi(file_ui, self)
        
        self.button_set_filter.clicked.connect( self.set_filter )
        self.button_default_filter.clicked.connect( self.update_database )

        self.combobox_tarea.activated.connect( self.set_tarea_id )
        self.checkbox_tarea.stateChanged.connect( self.set_tarea_id )

        self.combobox_recurso.activated.connect( self.set_recurso_id )
        self.checkbox_recurso.stateChanged.connect( self.set_recurso_id )
        
        self.checkbox_datetime_range.stateChanged.connect( self.set_datetime_range )
        self.start_datetime.dateTimeChanged.connect( self.set_datetime_range )
        self.end_datetime.dateTimeChanged.connect( self.set_datetime_range )

        self.dict_datetime = { "start_datetime": None, "end_datetime": None }

        self.current_tarea_id = None
        self.current_recurso_id = None
        self.current_table_columns = []
        
        self.update_database()
        
        
    def current_datetime(self):
        # Primer dia del mes
        datetime_formatted = get_first_day_of_the_month()

        qdate = QDate.fromString(
            get_date_from_formatted_datetime( datetime_formatted ), 
            "yyyy-MM-dd" 
        )
        qtime = QTime.fromString( 
            get_time_from_formatted_datetime( datetime_formatted ), 
            "HH:mm:ss" 
        )

        self.start_datetime.setDate(qdate)
        self.start_datetime.setTime(qtime)
        
        # Ultimo dia del mes
        datetime_formatted = get_end_day_of_the_month()
        qdate = QDate.fromString(
            get_date_from_formatted_datetime( datetime_formatted ), 
            "yyyy-MM-dd" 
        )
        qtime = QTime.fromString( 
            get_time_from_formatted_datetime( datetime_formatted ), 
            "HH:mm:ss" 
        )
        self.end_datetime.setDate(qdate)
        self.end_datetime.setTime(qtime)
        
        
    def clear_parameter(self):
        # Restablecer todos valores al default.
        self.checkbox_tarea.setChecked( False )
        self.checkbox_recurso.setChecked( False )
        self.checkbox_datetime_range.setChecked( True )
        self.checkbox_soft_delete.setChecked( False ) 
        self.combobox_tarea.setCurrentIndex( 0 )
        self.combobox_recurso.setCurrentIndex( 0 )
        self.current_datetime()
    
    
    def set_tarea_id(self):
        self.current_tarea_id = None
        if self.checkbox_tarea.isChecked():
            current_id = self.combobox_tarea.currentData()
            if isinstance(current_id, int):
                self.current_tarea_id = current_id
    
    
    def set_recurso_id(self):
        self.current_recurso_id = None
        if self.checkbox_recurso.isChecked():
            current_id = self.combobox_recurso.currentData()
            if isinstance(current_id, int):
                self.current_recurso_id = current_id
                
                
    def set_datetime_range(self):
        if self.checkbox_datetime_range.isChecked():
            # Obtener parametros relacionados al tiempo
            # Start `qdate` `qtime`
            start_qdatetime = self.start_datetime.dateTime()
            
            start_qdate = self.start_datetime.date()
            start_date_str = str( start_qdate.toPyDate() )

            start_qtime = self.start_datetime.time()
            start_time_str = start_qtime.toString("HH:mm:ss")
            
            start_datetime_str = f"{start_date_str}T{start_time_str}"
            
            # End `qdate` `qtime`
            end_qdate = self.end_datetime.date()
            end_date_str = str( end_qdate.toPyDate() )
            
            end_qtime = self.end_datetime.time()
            end_time_str = end_qtime.toString("HH:mm:ss")
            
            end_datetime_str =  f"{end_date_str}T{end_time_str}"

            # Dict
            self.dict_datetime["start_datetime"] = start_datetime_str
            self.dict_datetime["end_datetime"] = end_datetime_str
        else:
            self.dict_datetime["start_datetime"] = None
            self.dict_datetime["end_datetime"] = None
    
    
    def refresh_combobox(self):
        # Establecer combobox
        self.combobox_tarea.clear()
        for value in tarea_controller.get_all_values_without_soft_delete():
            self.combobox_tarea.addItem( value[1], userData=value[0] ) # descripcción, id
            
        self.combobox_recurso.clear()
        for value in recurso_controller.get_all_values_without_soft_delete():
            self.combobox_recurso.addItem( value[1], userData=value[0] ) # descripcción, id
    
    
    def refresh_table(self):
        # Actualizar datos de la tabla.
        all_column = actividad_controller.get_columns_for_the_view()
        self.table.clear()
        self.table.setColumnCount( len(all_column) )
        self.table.setHorizontalHeaderLabels( all_column )
        self.table.resizeColumnsToContents() # Establecer tamaño de columnas basado en sus nombres.
        
        all_value = self.current_table_columns
        self.table.setRowCount( len(all_value) )

        total_hours = 0
        number = 0
        for column in all_column:
            for row in range(0, len(all_value)):
                final_text = str
                if number == len(all_column)-1:
                    if all_value[row][number] == 1:
                        final_text = "Si"
                    else:
                        final_text = "No"
                else:
                    final_text = str(all_value[row][number])
                
                # Determinar horas
                if number == 8:
                    total_hours += all_value[row][number]
                
                # Agregar item
                self.table.setItem( row, number, QTableWidgetItem( final_text ) )

                # Establecer ancho y alto de filas tipo string.
                if isinstance( all_value[row][number], str ):
                    self.table.setColumnWidth(number, num_text_column_width)
                    
            number += 1
        
        # Establecer horas.
        self.entry_total_hours.setText( str(total_hours) )
    
    

    def set_filter(self):
        self.current_table_columns = actividad_controller.filtered_query_for_the_view( 
            start_datetime=self.dict_datetime["start_datetime"],
            end_datetime=self.dict_datetime["end_datetime"],
            TareaId=self.current_tarea_id, RecursoHumanoId=self.current_recurso_id,
            Baja=self.checkbox_soft_delete.isChecked()
        )
        self.refresh_table()
    
    
    def update_database(self):
        self.clear_parameter()
        self.refresh_combobox()
        self.set_tarea_id()
        self.set_recurso_id()
        self.set_datetime_range()
        self.set_filter()