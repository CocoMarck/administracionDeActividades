from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem
)
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
    def __init__(self):
        super().__init__()

        uic.loadUi(file_ui, self)