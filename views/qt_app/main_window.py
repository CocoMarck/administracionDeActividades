from PyQt6 import QtWidgets, uic
from views.interface.interface_number import *
from views.interface.css_util import text_widget_style, get_list_text_widget
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
        margin_based_font=True, padding=num_space_padding, idented=4
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
        
        self.init_all()
    
    def init_text(self):
        print(self.label_id.text())
    
    def init_table(self):
        all_column = tarea_table.get_all_column()
        self.table.clear()
        self.table.setColumnCount( len(all_column) )
        self.table.setHorizontalHeaderLabels( all_column )
        
        all_value = tarea_table.get_all_value()
        self.table.setRowCount( len(all_value) )
        number = 0
        for column in all_column:
            for row in range(0, len(all_value)):
                self.table.setItem( row, column, str(all_value[number][row]) )
            number += 1
    
    def init_all(self):
        self.init_table()
        self.init_text()
    
    def add(self):
        pass
    
    def cancel(self):
        self.entry_id.clear()
        self.entry_description.clear()