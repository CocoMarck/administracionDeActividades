# Notas
**Recuerda esto**:
- path = /conjunto-de-directorios/archivo.conExtension
- ruta/directorio = /conjunto/de/directorios
- file=archivo.conExtension

## StandardDataBase
Hacer objeto modelo para manejar sqlite db, estandar.
**StandardDataBase**. Nombre de archivo **standard_database.py**

**Parametros**: 
- name_dir_data
- name_db

**Tendra los atributos**:
- dir_current
- name_dir_data
- dir_data
- name_database
- path_database

**Tendra las funciones**:
- set_directory_data(self) -> os.path:
*Depende de current_dir y name_dir_data. Cambia atributo dir_data*

- set_database_path(): -> os.path:
*Depende de dir_data. Cambia path_database*

- connect() -> sqlite3.connect:
*Se conectara a path_database.*

- execute_statement( sql_statement=str, commit=bool, verbose=bool ) -> bool:
*sql_statement. Instrucción.
verbose. Este parametro es para mostrar la instrucción.
commit. Este parametro es para cometer los cambios.*

- create_database() -> bool:
*Depende de connect()
Solo creara una db vacia. Se creara con la función connect*

- create_table_parameter( table=string, sql_statement= str | list ) -> None:
*Depende de execute_statement()
Para crear tablas. (solo poner statement de parametros para crear tablas). Se creara con un IF NOT EXITS
Esta función permitira parametros; 
table = string. Nombre de tabla a crear.
sql_statement. Este parametro podra ser una lista o un string.*

- remove_table(table: str):
*Depende de execute_statement()
Remueve tabla.*
