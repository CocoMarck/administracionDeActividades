import models
import controllers
import sys
from PyQt6.QtWidgets import QApplication
from views.qt_app.main_window import MyApp, qss_style
from views.qt_app.tarea_form import TareaForm




# Iniciar DB
administrar_actividad = controllers.AdministracionDeActividadController( verbose=True )
administrar_actividad.start_database(); print()
administrar_actividad.tables(); print()
#administrar_actividad.delete_database()




#print(qss_style); print()
def main():
    app = QApplication( sys.argv )
    app.setStyleSheet( qss_style )
    
    # Crear la ventana principal
    window = MyApp()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()