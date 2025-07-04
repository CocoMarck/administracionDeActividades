from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem
)
from views.interface.interface_number import *
from views.interface.css_util import text_widget_style, get_list_text_widget
from core.text_util import ignore_text_filter, pass_text_filter

from .tarea_form import TareaForm
from .recurso_form import RecursoForm
from .actividad_form import ActividadForm
from .actividad_query_form import ActividadQueryForm
from utils import ResourceLoader
import sys, os


# Directorio
resource_loader = ResourceLoader()
dir_views = resource_loader.get_base_path( 'views' )
dir_ui = dir_views.joinpath( 'ui' )
file_ui = dir_ui.joinpath( 'main_window.ui' )


# Estilo
font = "Liberation Mono"
qss_style = ''
for widget in get_list_text_widget( 'Qt' ):
    qss_style += text_widget_style(
        widget=widget, font=font, font_size=num_font, 
        margin_based_font=False, padding=num_space_padding, idented=4,
        margin_xy=num_margin_xy
    )
# Agregar limite de ancho de combobox.
#'''
qss_style += (
    "\nQComboBox{\n"
    f"    min-width: {num_combobox_width}px;\n"
    f"    max-width: {num_combobox_width}px;\n"
    "}"
)
#'''


# Ventana
class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize( nums_win_main[0], nums_win_main[1])
        self.setWindowTitle( "Ventana principal" )
        uic.loadUi(file_ui, self)
        
        # Agregar Formularios | Ventanas
        self.tarea_form = TareaForm()
        self.tab_widget.addTab( self.tarea_form, "Tarea" ) # index 0
        
        self.recurso_form = RecursoForm()
        self.tab_widget.addTab( self.recurso_form, "Recurso Humano" ) # index 1
        
        self.actividad_form = ActividadForm()
        self.tab_widget.addTab( self.actividad_form, "Actividad" ) # index 2
        
        self.actividad_query_form = ActividadQueryForm()
        self.tab_widget.addTab( self.actividad_query_form, "Consulta Actividad" ) # index 3
        
        # Detectar cambio de tab
        self.tab_widget.currentChanged.connect( self.on_tab_changed )
    
    def on_tab_changed(self, index):
        '''
        Refrescar tab, dependiendo de su index
        '''
        if index == 0:
            self.tarea_form.update_database()
        elif index == 1:
            self.recurso_form.update_database()
        elif index == 2:
            self.actividad_form.update_database()
        elif index == 3:
            self.actividad_query_form.update_database()