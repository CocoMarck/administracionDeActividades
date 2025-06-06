from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem
)
from views.interface.interface_number import *
from core.util_text import ignore_text_filter, pass_text_filter
import controllers
import sys, os


# Directorio
dir_current = os.path.dirname( os.path.abspath(sys.argv[0]) )
dir_views = os.path.join( dir_current, 'views')
dir_ui = os.path.join( dir_views, 'ui')
file_ui = os.path.join( dir_ui, 'recurso_form.ui')



# Ventana
class RecursoForm(QtWidgets.QWidget):
    def __init__(
        self, table_controller=controllers.RecursoHumanoController( verbose=True, return_message=False )
    ):
        super().__init__()
        self.resize( nums_win_main[0], nums_win_main[1])
        uic.loadUi(file_ui, self)
        
        self.current_id = None
        
        self.table_controller = table_controller
        
        self.entry_id.textChanged.connect( self.on_text_changed )
        self.button_add.clicked.connect( self.insert_user )
        self.button_update.clicked.connect( self.update_user )
        
        self.refresh_all()
        

    def on_text_changed(self, text):
        # Solo aceptar numeros en el entry
        self.entry_id.setText( ignore_text_filter(text, "1234567890")  )
        
        # Determinar que se escribio un id
        self.entry_name.setText( "" )
        self.entry_paternal_surname.setText( "" )
        self.entry_maternal_surname.setText( "" )
        self.entry_position.setText( "" )
        self.checkbox_soft_delete.setChecked( False )
        if self.entry_id.text() != '':
            self.current_id = int(self.entry_id.text()) 

            # Establecer descripcción y baja por medio del id
            for column in self.table_controller.get_all_value():
                if self.current_id == column[0]:
                    self.entry_name.setText( column[1] )
                    self.entry_paternal_surname.setText( column[2] )
                    self.entry_maternal_surname.setText( column[3] )
                    self.entry_position.setText( column[4] )
                    self.checkbox_soft_delete.setChecked( bool(column[11]) )
                    break
        else:
            self.current_id = None
    
    
    def refresh_text(self):
        self.label_id.setText( "RecursoHumanoId" )
        self.label_name.setText( "Nombre" )
        self.label_paternal_surname.setText( "Apellido paterno" )
        self.label_maternal_surname.setText( "Apellido materno" )
        self.label_position.setText( "Puesto" )
        self.label_soft_delete.setText( "Baja" )
        self.button_add.setText( "Agregar" )
        self.button_update.setText( "Actualizar" )
        self.button_cancel.setText( "Cancelar" )


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
                    if all_value[row][number] == 1:
                        final_text = "Si"
                    else:
                        final_text = "No"
                else:    
                    final_text = str(all_value[row][number])
                    
                self.table.setItem( row, number, QTableWidgetItem( final_text ) )
                    
            number += 1
    
    
    def refresh_all(self):
        self.refresh_text()
        self.refresh_table()
    
    
    def insert_user(self):
        self.table_controller.insert_user(
            Nombre=self.entry_name.text(), APP=self.entry_paternal_surname.text(), 
            APM=self.entry_maternal_surname.text(), Puesto=self.entry_position.text()
        )
        self.refresh_table()
    
    
    def update_user(self):
        if isinstance( self.current_id, int ):
            self.table_controller.update_user(
                RecursoHumanoId=self.current_id, 
                Nombre=self.entry_name.text(), APP=self.entry_paternal_surname.text(), 
                APM=self.entry_maternal_surname.text(), Puesto=self.entry_position.text(),
                Baja=self.checkbox_soft_delete.isChecked()
            )
            self.refresh_table()