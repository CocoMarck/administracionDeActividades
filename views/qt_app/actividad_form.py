from views.interface.interface_number import *
from core.text_util import ignore_text_filter, pass_text_filter
from core import time_util
from utils import ResourceLoader

from models.database_names import RECURSOHUMANO_TABLE_NAMES, TAREA_TABLE_NAMES, ACTIVIDAD_TABLE_NAMES
from controllers.table_controller import get_datetime
import controllers

from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import ( QTableWidget, QTableWidgetItem )
from PyQt6.QtCore import QDate, QDateTime, QTime, QSize




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
        
        # Eventos
        self.button_save.clicked.connect( self.save_actividad )
        self.button_cancel.clicked.connect( self.update_database )
        self.entry_id.textChanged.connect( self.on_text_changed )

        self.start_date.dateTimeChanged.connect( self.set_hours )
        self.end_date.dateTimeChanged.connect( self.set_hours )
        
        self.refresh_text()
        self.refresh_table()
        self.refresh_combobox()
        self.current_date()
        
        
    def current_date(self):
        '''
        Establecer fecha y tiempo actual
        '''
        qdate = QDate.fromString( get_datetime( "date" ), "yyyy-MM-dd" )
        qtime = QTime.fromString( get_datetime( "time" ), "HH:mm:ss" )
        self.start_date.setDate(qdate)
        self.start_date.setTime(qtime)
        self.end_date.setDate(qdate)
        self.end_date.setTime(qtime)
    
    
    def clear_parameter(self):
        '''
        Dejar en parametros en default
        '''
        self.entry_note.clear()
        self.entry_id.clear()
        self.combobox_tarea.setCurrentIndex( 0 )
        self.combobox_recurso.setCurrentIndex( 0 )
        self.current_date()
        self.label_time_hours.setText( "0" )
        self.checkbox_soft_delete.setChecked( False )
    

    def refresh_text(self):
        # Establecer texto
        self.label_id.setText( "ActividadId" )
        self.label_start_date.setText( "Fecha inicio" )
        self.label_end_date.setText( "Fecha fin" )
        self.label_note.setText( "Nota" )
        self.label_hours.setText( "Horas" )
        self.label_tarea.setText( "Tarea" )
        self.label_recurso.setText( "Recurso humano" )
        self.button_save.setText( "Guardar" )
        

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
        all_column = self.table_controller.get_columns_for_the_view()
        self.table.clear()
        self.table.setColumnCount( len(all_column) )
        self.table.setHorizontalHeaderLabels( all_column )
        self.table.resizeColumnsToContents() # Para que se acomode por el texto columna.
        
        all_value = self.table_controller.get_values_for_the_view()
        self.table.setRowCount( len(all_value) )
        number = 0
        for column in all_column:
            for row in range(0, len(all_value)):
                final_text = str
                if number == len(all_column) -1 :
                    if all_value[row][number] == 1:
                        final_text = "Si"
                    else:
                        final_text = "No"
                else:
                    final_text = str(all_value[row][number])
                    
                self.table.setItem( row, number, QTableWidgetItem( final_text ) )
                    
            number += 1
    
            
    def refresh_parameter(self):
        default_parameter = False
        
        if isinstance( self.current_id, int ):
            # Establecer parametros por medio del id
            for column in table_actividad.get_all_values():
                if self.current_id == column[0]:
                    default_parameter = False
                
                    self.entry_note.setText( column[3] )

                    # Combos
                    tarea_index = self.combobox_tarea.findData( column[1] )
                    self.combobox_tarea.setCurrentIndex( tarea_index )
                    
                    recurso_index = self.combobox_recurso.findData( column[2] )
                    self.combobox_recurso.setCurrentIndex( recurso_index )

                    # Date Time
                    start_datetime = column[4].split( "T" )
                    self.start_date.setDate( QDate.fromString( start_datetime[0], "yyyy-MM-dd" ) )
                    self.start_date.setTime( QTime.fromString( start_datetime[1], "HH:mm:ss") )
                    
                    end_datetime = column[5].split( "T" )
                    self.end_date.setDate( QDate.fromString( end_datetime[0], "yyyy-MM-dd" ) )
                    self.end_date.setTime( QTime.fromString( end_datetime[1], "HH:mm:ss") )
                                       
                    # Hora
                    self.label_time_hours.setText( str(column[6]) )

                    # Checkbox
                    self.checkbox_soft_delete.setChecked( bool(column[13]) )
                    break

                else:
                    default_parameter = True
        else:
            default_parameter = True
        
        if default_parameter:
            self.current_date()
            self.clear_parameter()
    
    
    def refresh_all(self):
        self.refresh_text()
        self.refresh_table()
        self.refresh_parameter()
        self.refresh_combobox()
    
    
    def on_text_changed(self, text):
        '''
        Detectar cambio de id. Actualizar parametros
        '''
        # Solo aceptar numeros en el entry
        self.entry_id.setText( ignore_text_filter(text, "1234567890")  )
        
        # Determinar que se escribio un id
        self.checkbox_soft_delete.setChecked( False )
        if self.entry_id.text() != '':
            self.current_id = int(self.entry_id.text()) 
        else:
            self.current_id = None
        self.refresh_parameter()
    
    
    def dict_date_time(self):
        # Obtener parametros relacionados al tiempo
        
        # Start `qdate` `qtime`
        start_qdate = self.start_date.date()
        start_date_str = str( start_qdate.toPyDate() )

        start_qtime = self.start_date.time()
        start_time_str = start_qtime.toString("HH:mm:ss")
        
        start_datetime_str = f"{start_date_str}T{start_time_str}"
        
        # End `qdate` `qtime`
        end_qdate = self.end_date.date()
        end_date_str = str( end_qdate.toPyDate() )
        
        end_qtime = self.end_date.time()
        end_time_str = end_qtime.toString("HH:mm:ss")
        
        end_datetime_str =  f"{end_date_str}T{end_time_str}"
        
        
        # Obtener dias qdate
        # `dayOfYear()`, no detecta años, solo dias. 
        # `QDate.year()`, para detectar años. (No toma en cuenta el año visiesto.
        # `daysInYear()` Dias en un año deteminado
        # Obtener milisegundso qtime
        # Detrminar total de dias, y horas
        start_end_year = [start_qdate.year(), end_qdate.year()]
        year_day = ( max(start_end_year) - min(start_end_year) ) * 365

        start_end_day = [start_qdate.dayOfYear(), end_qdate.dayOfYear()]
        total_day = max(start_end_day) - min(start_end_day) + (year_day)        
        
        
        # Determinar cual fecha es mayor.
        start_qtime_msecs = start_qtime.msecsSinceStartOfDay() 
        end_qtime_msecs = end_qtime.msecsSinceStartOfDay()
        
        if start_qtime_msecs < end_qtime_msecs:
            # Start < End
            start_end_time = [ end_qtime_msecs, start_qtime_msecs ]
    
            start_ready_datetime = start_datetime_str
            end_ready_datetime = end_datetime_str

        else:
            # Start > End, or Start==End
            start_end_time = [ start_qtime_msecs, end_qtime_msecs ]

            start_ready_datetime = end_datetime_str
            end_ready_datetime = start_datetime_str
        
        
        # Diferencia entre fechas en milisegundos.
        # Se podria usar `max() -min()`, pero mejor directo. Menos procesamiento.
        total_time = start_end_time[0] - start_end_time[1]
        
        
        # Usando función `time_util.get_time()`
        total_hour = (
            time_util.get_time( total_time, "millisecond", "hour" ) +
            time_util.get_time( total_day, "day", "hour" )
        )
        
        
        # Dict
        dict_ready = {
            "start_datetime" : start_ready_datetime,
            "end_datetime" : end_ready_datetime,
            "hours" : float(total_hour)
        }
        
        return dict_ready
    

    def set_hours(self):
        dict_time = self.dict_date_time()
        self.label_time_hours.setText( str(dict_time["hours"]) )
    
    
    def update_database(self):
        self.refresh_combobox()
        self.refresh_table()
        self.clear_parameter()
    

    def insert_actividad(self):
        # Insertar actividad
        date_time = self.dict_date_time()

        table_actividad.insert_actividad(
            TareaId=self.combobox_tarea.currentData(), 
            RecursoHumanoId=self.combobox_recurso.currentData(), NOTA=self.entry_note.text(), 
            FechaInicio=date_time["start_datetime"], FechaFin=date_time["end_datetime"],
            HORAS=date_time["hours"]
        )
        self.refresh_table()
        self.clear_parameter()
    

    def update_actividad(self):
        # Actualizar actividad
        date_time = self.dict_date_time()
        
        table_actividad.update_actividad(
            ActividadId=self.current_id, 
            TareaId=self.combobox_tarea.currentData(), 
            RecursoHumanoId=self.combobox_recurso.currentData(), 
            NOTA=self.entry_note.text(), FechaInicio=date_time["start_datetime"], 
            FechaFin=date_time["end_datetime"], HORAS=date_time["hours"], UsuarioId=0, 
            Baja=int(self.checkbox_soft_delete.isChecked())
        )
        self.refresh_table()
        #self.refresh_parameter()
        self.clear_parameter()
    
    
    def save_actividad(self):
        if isinstance( self.current_id, int):
            self.update_actividad()
        else:
            self.insert_actividad()