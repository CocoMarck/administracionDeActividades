# Notas
**Definición de conceptos relacionados con los archivos**:
- path = /conjunto-de-directorios/archivo.conExtension
- ruta/directorio = /conjunto/de/directorios
- file=archivo.conExtension




# Hacer formulario/app-gui, por cada tabla  
Tabla Tarea, Tabla Recursos Humanos, Tabla Actividad  
```
views/
    ui/
        main_window.ui
        tarea_form.ui
        recurso_form.ui
        actividad_form.ui
    qt_app/
        tarea_tab.py
        recurso_tab.py
        actividad_tab.py
        main_window.py # La ventana principal, que permite acceder a las tablas. Con pestañas.
    
main.py # El que inciara todo.
```



# Metodos para TareaTable y TareaController  
> Hacer los mismos metodos del TareaTable para el TareaController, pero el TareaController es aprueba de errores, y sirve como debug.  
Primero se hacen los metodos del TareaTable y despues los del TareaController.

- Método para obtener una fila por el id. `get_row_by_id()`
- Hacer una función para obtener valor de fila, por medio del nombre de la columna. `get_value_by_column()`  
Puede ser nombre de columna, o por valor int de la columna, su index.




# Para la tarea `table` y `controller` `FechaCreacion FechaModifciacion FechaBaja`
*La tabla tarea tiene estos campos*  
**Todas las fechas seran estilo `00-00-00`**  
- Cuando se inserte/agrege una tarea. `insert_tarea`, Se establecera una `FechaCreacion`.  
- Cuando se actualice una tarea. `update_tarea`, Se establecera una `FechaModificacion`.  
- Cuando se de baja una tarea. Se establecera una `FechaBaja`.  

Todas los id de las fechas seran por defecto 0.




# Establecer modulo para manejar los directorios del proyecto
Este modulo se llama `resource_loader.py`




# Establecer variables de nombres
**Establecer las variables necesarias para esblecer los nombres relacionados con la base de datos AdministracionDeActividad:** `name_administracion_actividad, name_tarea, name_actividad, name_recurso_humano, name_directory`
Poner esto en `config/administracion_actividad_config.py`

**Para el StandardDataBase y StandardTable:** `name_directory`
Poner esto en `config/database_config.py`




## Restructurar language.py a (Esto se hara en el repo MultiIdiomaTest): 
`language_model.py, language_controller.py, language_service.py`
- Model para funciones para manejar la db. 
- Controler para manejar model de manera segura. 
- Service unificar model y controler




## StandardDataBase (Esto ya esta hecho, hasta tiene mas metodos)
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

- get_all_column(table) -> list | None:
*Devolver todas las columnas de una tabla*