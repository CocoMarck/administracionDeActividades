from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem
)
from views.interface.interface_number import *
from core.text_util import ignore_text_filter, pass_text_filter
from utils import ResourceLoader
import controllers
import sys, os

from utils.wrappers.language_wrapper import get_text


# Directorio
resource_loader = ResourceLoader()
dir_views = resource_loader.get_base_path( 'views' )
dir_ui = dir_views.joinpath( 'ui' )
file_ui = dir_ui.joinpath( 'recurso_form.ui' )


# Ventana
class RecursoForm(QtWidgets.QWidget):
    def __init__(
        self, table_controller=controllers.RecursoHumanoController( verbose=True )
    ):
        super().__init__()
        self.resize( nums_win_main[0], nums_win_main[1])
        uic.loadUi(file_ui, self)
        
        self.current_id = None
        
        self.table_controller = table_controller
        
        self.entry_id.textChanged.connect( self.on_text_changed )
        self.button_save.clicked.connect( self.save_user )
        self.button_cancel.clicked.connect( self.update_database )
        
        self.refresh_all()
    
    
    
    def clear_parameter(self):
        self.entry_id.setText("")
        self.entry_name.setText( "" )
        self.entry_paternal_surname.setText( "" )
        self.entry_maternal_surname.setText( "" )
        self.entry_position.setText( "" )
        self.checkbox_soft_delete.setChecked( False )
    
    
    def refresh_text(self):
        self.label_id.setText( get_text("id") )
        self.label_name.setText( get_text("name") )
        self.label_paternal_surname.setText( get_text("paternal-surname") )
        self.label_maternal_surname.setText( get_text("maternal-surname") )
        self.label_position.setText( get_text("workstation") )
        self.label_soft_delete.setText( get_text("low") )
        self.button_save.setText( get_text("save") )
        self.button_cancel.setText( get_text("cancel") )


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
                if number == len(all_column)-1:
                    if all_value[row][number] == 1:
                        final_text = "Si"
                    else:
                        final_text = "No"
                else:    
                    final_text = str(all_value[row][number])
                    
                self.table.setItem( row, number, QTableWidgetItem( final_text ) )
                
                # Establecer ancho de filas tipo string.
                if isinstance( all_value[row][number], str ):
                    self.table.setColumnWidth(number, num_text_column_width)
                    
            number += 1
        
        
    def refresh_parameter(self):
        '''
        Establecer parametros, dependiendo del id main
        '''
        default_parameter = False
        if isinstance( self.current_id, int ):
            # Establecer descripcción y baja por medio del id
            for column in self.table_controller.get_all_values():
                if self.current_id == column[0]:
                    default_parameter = False
                
                    self.entry_name.setText( column[1] )
                    self.entry_paternal_surname.setText( column[2] )
                    self.entry_maternal_surname.setText( column[3] )
                    self.entry_position.setText( column[4] )
                    self.checkbox_soft_delete.setChecked( bool(column[11]) )
                    break
                else:
                    default_parameter = True
        else:
            default_parameter = True
        
        if default_parameter:
            self.clear_parameter()
    
    
    def refresh_all(self):
        self.refresh_text()
        self.refresh_table()
        self.refresh_parameter()
        
        
    def on_text_changed(self, text):
        '''
        Establecer id main
        '''
        # Solo aceptar numeros en el entry
        self.entry_id.setText( ignore_text_filter(text, "1234567890")  )
        
        # Determinar que se escribio un id
        if self.entry_id.text() != '':
            self.current_id = int(self.entry_id.text()) 
        else:
            self.current_id = None
        self.refresh_parameter()
    
    
    def insert_user(self):
        self.table_controller.insert_user(
            Nombre=self.entry_name.text(), APP=self.entry_paternal_surname.text(), 
            APM=self.entry_maternal_surname.text(), Puesto=self.entry_position.text()
        )
        self.clear_parameter()
        self.refresh_table()
    
    
    def update_user(self):
        if isinstance( self.current_id, int ):
            self.table_controller.update_user(
                RecursoHumanoId=self.current_id, 
                Nombre=self.entry_name.text(), APP=self.entry_paternal_surname.text(), 
                APM=self.entry_maternal_surname.text(), Puesto=self.entry_position.text(),
                Baja=self.checkbox_soft_delete.isChecked()
            )
            self.clear_parameter()
            self.refresh_table()
    
    def save_user(self):
        if isinstance( self.current_id, int ):
            self.update_user()
        else:
            self.insert_user()
            
            
    def update_database(self):
        self.refresh_table()
        self.clear_parameter()