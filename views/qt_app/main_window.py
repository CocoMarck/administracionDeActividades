from views.interface.interface_number import *
from views.interface.css_util import text_widget_style, get_list_text_widget
from core.text_util import ignore_text_filter, pass_text_filter

from .tarea_form import TareaForm
from .recurso_form import RecursoForm
from .actividad_form import ActividadForm
from .actividad_query_form import ActividadQueryForm
from utils import ResourceLoader

from utils.wrappers.language_wrapper import get_text

from controllers import LanguageConfigTableController

import sys, os
from functools import partial

from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem
)
from PyQt6.QtGui import QIcon, QAction


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

language_config_table = LanguageConfigTableController()




# Ventana
class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize( nums_win_main[0], nums_win_main[1])
        uic.loadUi(file_ui, self)
        
        # Agregar Formularios | Ventanas
        self.tarea_form = TareaForm()
        self.tab_widget.addTab( self.tarea_form, get_text("task") ) # index 0
        
        self.recurso_form = RecursoForm()
        self.tab_widget.addTab( self.recurso_form, get_text("human-resource") ) # index 1
        
        self.actividad_form = ActividadForm()
        self.tab_widget.addTab( self.actividad_form, get_text("activity") ) # index 2
        
        self.actividad_query_form = ActividadQueryForm()
        self.tab_widget.addTab( self.actividad_query_form, get_text("activity-query") ) # index 3        
        
        # Detectar cambio de tab
        self.tab_widget.currentChanged.connect( self.on_tab_changed )
        
        # Texto
        self.refresh_text()
        self.refresh_languages()
    
    
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
    
    
    def refresh_text(self):
        self.setWindowTitle( get_text("ada") )
        self.tab_widget.setTabText( 0, get_text("task") )
        self.tab_widget.setTabText( 1, get_text("human-resource") )
        self.tab_widget.setTabText( 2, get_text("activity") )
        self.tab_widget.setTabText( 3, get_text("activity-query") )
        self.menu_language.setTitle( get_text("language") )
    
    
    def refresh_all_text(self):
        self.refresh_text()
        self.recurso_form.refresh_text()
        self.tarea_form.refresh_text()
        self.actividad_form.refresh_text()
        self.actividad_query_form.refresh_text()
    
    
    def refresh_languages(self):
        language_list = language_config_table.get_list_of_languages()
        for language in language_list:
            action = QAction( text=language, parent=self )
            action.triggered.connect( partial( self.set_language, language=language ) )
            self.menu_language.addAction(  action )
    
    
    def set_language(self, language:str):
        language_config_table.update_language( language )
        self.refresh_all_text()