import models
import controllers



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
database.delete_database()

administrar_actividad = models.AdministracionDeActividad()
print( administrar_actividad.start_database() )
print( administrar_actividad.tables() )
print( administrar_actividad.exists_table( table="TAREA" ) )