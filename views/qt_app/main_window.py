from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem
)
from views.interface.interface_number import *
from views.interface.css_util import text_widget_style, get_list_text_widget
from core.util_text import ignore_text_filter, pass_text_filter
import controllers
import sys, os


# Directorio
dir_current = os.path.dirname( os.path.abspath(sys.argv[0]) )
dir_views = os.path.join( dir_current, 'views')
dir_ui = os.path.join( dir_views, 'ui')
file_ui = os.path.join( dir_ui, 'window.ui')


# Estilo
font = "Liberation Mono"
qss_style = ''
for widget in get_list_text_widget( 'Qt' ):
    qss_style += text_widget_style(
        widget=widget, font=font, font_size=num_font, 
        margin_based_font=False, padding=num_space_padding, idented=4,
        margin_xy=num_margin_xy
    )


# Ventana
tarea_table = controllers.TareaController( verbose=True, return_message=False )
class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize( nums_win_main[0], nums_win_main[1])
        uic.loadUi(file_ui, self)
        
        self.button_cancel.clicked.connect( self.cancel )
        self.button_add.clicked.connect( self.add )
        self.button_update.clicked.connect(self.update)
        self.entry_id.textChanged.connect(self.on_text_changed)
        
        self.refresh_all()
    
    def on_text_changed(self, text):
        # Solo aceptar numeros en el entry
        self.entry_id.setText( ignore_text_filter(text, "1234567890")  )
        
        # Determinar que se escribio un id
        if self.entry_id.text() != '':
            id_search = int(self.entry_id.text()) 

            # Establecer descripcción y baja por medio del id
            self.entry_description.setText( "" )
            for column in tarea_table.get_all_value():
                if id_search == column[0]:
                    self.entry_description.setText( column[1] )
                    self.checkbox_soft_delete.setChecked( bool(column[8]) )
                    break
                    
                    
    
    def refresh_text(self):
        # Actualizar texto de widgets
        self.label_id.setText( "TareaId" )
        self.label_description.setText( "Descripción" )
        self.label_soft_delete.setText( "Baja" )
        self.button_add.setText( "Agregar" )
        self.button_update.setText( "Actualizar" )
        self.button_cancel.setText( "Cancelar" )
    
    def refresh_table(self):
        # Actualizar datos de la tabla.
        all_column = tarea_table.get_all_column()
        self.table.clear()
        self.table.setColumnCount( len(all_column) )
        self.table.setHorizontalHeaderLabels( all_column )
        self.table.resizeColumnsToContents() # Para que se acomode por el texto columna.
        
        all_value = tarea_table.get_all_value()
        self.table.setRowCount( len(all_value) )
        number = 0
        for column in all_column:
            for row in range(0, len(all_value)):
                self.table.setItem( row, number, QTableWidgetItem( str(all_value[row][number]) ) )
            number += 1
    
    def refresh_all(self):
        # Actualizar todo lo posible
        self.refresh_table()
        self.refresh_text()
    
    def add(self):
        # Insertar en la tabla
        if tarea_table.insert_tarea( self.entry_description.text() ):
            self.refresh_table()
    
    def update(self):
        # Actualizar en la tabla
        if self.entry_id.text() != "":
            if tarea_table.update_tarea(
                int(self.entry_id.text()), self.entry_description.text(), 
                int(self.checkbox_soft_delete.isChecked())
            ):
                self.refresh_table()
        
    
    def cancel(self):
        # Borrat todo el texto
        self.entry_id.clear()
        self.entry_description.clear()