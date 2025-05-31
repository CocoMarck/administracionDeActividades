import models
import controllers
import sys
from PyQt6.QtWidgets import QApplication
from views.qt_app.main_window import MyApp, qss_style


'''
database = controllers.DataBaseController( database=models.StandardDataBase( "example" ), verbose=True )
database.create_database()
database.execute_statement(
    "DROP TABLE IF EXISTS prueba;", 
    commit=False
)
database.execute_statement(
    """
CREATE TABLE IF NOT EXISTS prueba(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NULL,
    hour FLOAT NULL
);
    """, 
    commit=True
)
database.execute_statement(
    """
CREATE TABLE IF NOT EXISTS aguacate(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NULL,
    hour FLOAT NULL
);
    """, 
    commit=True
)
database.tables()
database.exists_table( "prueba" )
database.exists_table( "elCacas" )
database.delete_table( "aguacate" )
database.delete_table( "elCacas" )
#database.delete_database()

table=models.StandardTable( database=database, table="prueba" )
print(
    table.get_all_column(), '\n',
    table.get_all_value()
)
'''
# Iniciar DB
administrar_actividad = controllers.AdministracionDeActividadController( verbose=True, return_message=False)
administrar_actividad.start_database(); print()
administrar_actividad.tables(); print()
#administrar_actividad.delete_database()

tarea_table = controllers.TareaController( verbose=True, return_message=False )
#print( tarea_table.name )
tarea_table.get_all_column(); print()
tarea_table.get_all_value(); print()



#print(qss_style)
def main():
    app = QApplication(sys.argv)
    app.setStyleSheet( qss_style )
    
    # Crear la ventana principal
    window = MyApp()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()