from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem
)
from views.interface.interface_number import *
from views.interface.css_util import text_widget_style, get_list_text_widget
from core.util_text import ignore_text_filter, pass_text_filter

from .tarea_form import TareaForm
from .recurso_form import RecursoForm
import sys, os


# Directorio
dir_current = os.path.dirname( os.path.abspath(sys.argv[0]) )
dir_views = os.path.join( dir_current, 'views')
dir_ui = os.path.join( dir_views, 'ui')
file_ui = os.path.join( dir_ui, 'main_window.ui')


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
class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize( nums_win_main[0], nums_win_main[1])
        self.setWindowTitle( "Ventana principal" )
        uic.loadUi(file_ui, self)
        
        # Agregar Formularios | Ventanas
        self.tarea_form = TareaForm()
        self.tab_widget.addTab( self.tarea_form, "Tarea" )
        
        self.recurso_form = RecursoForm()
        self.tab_widget.addTab( self.recurso_form, "Recurso Humano" )