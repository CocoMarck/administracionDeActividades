import models

data_base = models.AdministracionDeActividad()
print( data_base.file_db )
data_base.create_db()

standard_database = models.StandardDataBase( "example" )
print( standard_database.path_database )
#print( standard_database.connect() )
#standard_database.execute_statement( sql_statement="", commit=False, verbose=True)
standard_database.create_database( verbose=True )

standard_database.create_table_parameter(
    table="prueba", sql_statement="hola TEXT NULL,\nadios TEXT NULL", commit=True, verbose=True
)
standard_database.create_table_parameter(
    table="prueba", sql_statement=["hola", "vatos"], commit=False, verbose=True
)
standard_database.create_table_parameter( 
    table="prueba", sql_statement=[ 
        ["hola", "vatos", "locos"],
        ["hola", "vatos", "locos"],
        ["hola", "vatos", "locos"]
    ], commit=False, verbose=True
)