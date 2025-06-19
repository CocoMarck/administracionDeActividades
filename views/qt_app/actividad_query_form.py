from views.interface.interface_number import *
from core.util_text import ignore_text_filter, pass_text_filter
from core import util_time
from utils import ResourceLoader
from controllers.table_controller import get_datetime
import controllers

from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import ( QTableWidget, QTableWidgetItem )
from PyQt6.QtCore import QDate, QDateTime, QTime




# Archivo ui
resource_loader = ResourceLoader()
dir_views = resource_loader.get_base_path( 'views' )
dir_ui = dir_views.joinpath( 'ui' )
file_ui = dir_ui.joinpath( 'actividad_query_form.ui' )





class ActividadQueryForm(QtWidgets.QWidget):
    def __init__( self, table_controller=None ):
        super().__init__()

        self.resize( nums_win_main[0], nums_win_main[1] )
        uic.loadUi(file_ui, self)