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

administrar_actividad = models.AdministracionDeActividad()
print( administrar_actividad.start_database() )