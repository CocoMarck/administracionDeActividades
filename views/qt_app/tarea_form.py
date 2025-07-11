from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem
)
from views.interface.interface_number import *
from core.text_util import ignore_text_filter, pass_text_filter
from utils import ResourceLoader

from utils.wrappers.language_wrapper import get_text

import controllers
import sys, os


# Directorio
resource_loader = ResourceLoader()
dir_views = resource_loader.get_base_path( 'views' )
dir_ui = dir_views.joinpath( 'ui' )
file_ui = dir_ui.joinpath( 'tarea_form.ui' )


# Ventana
tarea_table = controllers.TareaController( verbose=True )
class TareaForm(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize( nums_win_main[0], nums_win_main[1])
        uic.loadUi(file_ui, self)
        
        self.button_save.clicked.connect( self.save )
        self.button_cancel.clicked.connect( self.update_database )
        self.entry_id.textChanged.connect( self.on_text_changed )
        
        self.current_id = None
        
        self.refresh_all()
    
    def clear_parameter(self):
        '''
        Limpiar parametros
        '''
        self.entry_id.setText( "" )
        self.entry_description.setText( "" )
        self.checkbox_soft_delete.setChecked( False )
                    
    
    def refresh_text(self):
        # Actualizar texto de widgets
        self.label_id.setText( get_text("id") )
        self.label_description.setText( get_text("description") )
        self.label_soft_delete.setText( get_text("low") )
        self.button_save.setText( get_text("save") )
        self.button_cancel.setText( get_text("cancel") )
    
    
    def refresh_table(self):
        # Actualizar datos de la tabla.
        all_column = tarea_table.get_columns_for_the_view()
        self.table.clear()
        self.table.setColumnCount( len(all_column) )
        self.table.setHorizontalHeaderLabels( all_column )
        self.table.resizeColumnsToContents() # Para que se acomode por el texto columna.
        
        all_value = tarea_table.get_values_for_the_view()
        self.table.setRowCount( len(all_value) )
        number = 0
        for column in all_column:
            for row in range(0, len(all_value)):
                final_text = str
                if number == len(all_column)-1:
                    if all_value[row][number] == 1:
                        final_text = get_text("yes")
                    else:
                        final_text = get_text("no")
                else:    
                    final_text = str(all_value[row][number])
                    
                self.table.setItem( row, number, QTableWidgetItem( final_text ) )
                
                # Establecer ancho de filas tipo string.
                if isinstance( all_value[row][number], str ):
                    self.table.setColumnWidth(number, num_text_column_width)
                    
            number += 1
    
    
    def refresh_parameter(self):
        default_parameter = False

        if isinstance( self.current_id, int ):
            # Establecer descripcción y baja por medio del id
            for column in tarea_table.get_all_values():
                if self.current_id == column[0]:
                    default_parameter = False

                    self.entry_description.setText( column[1] )
                    self.checkbox_soft_delete.setChecked( bool(column[8]) )
                    break
                else:
                    default_parameter = True
        else:
            default_parameter = True

        if default_parameter:
            self.clear_parameter()
    
    
    def refresh_all(self):
        # Actualizar todo lo posible
        self.refresh_table()
        self.refresh_text()
    
    
    def on_text_changed(self, text):
        # Solo aceptar numeros en el entry
        self.entry_id.setText( ignore_text_filter(text, "1234567890")  )
        
        # Determinar que se escribio un id
        if self.entry_id.text() != '':
            self.current_id = int(self.entry_id.text()) 
        else:
            self.current_id = None
        self.refresh_parameter()
    

    def add(self):
        # Insertar en la tabla
        if tarea_table.insert_tarea( self.entry_description.text() ):
            self.refresh_table()
            self.clear_parameter()
    
   
    def update(self):
        # Actualizar en la tabla
        if isinstance(self.current_id, int):
            if tarea_table.update_tarea(
                int(self.entry_id.text()), self.entry_description.text(), 
                int(self.checkbox_soft_delete.isChecked())
            ):
                self.refresh_table()
                self.clear_parameter()
    

    def save(self):
        # Actualizar o insertar dato.
        if isinstance(self.current_id, int):
            self.update()
        else:
            self.add()
    
    
    
    def update_database( self ):
        self.refresh_table()
        self.clear_parameter()