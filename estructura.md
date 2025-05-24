# Estructura del programa

## Recordatorios
### Archivos ```__init__.py```
Estos archivos sirven para:
- Marcar directorios como paquetes Python
- Controlar qué se exporta cuando se hace from package import *

Ejemplo para ```models/__init__.py```:
```python
from .tarea_model import Tarea
from .recurso_model import RecursoHumano
from .actividad_model import Actividad
from .language_model import LanguageModel

__all__ = ['Tarea', 'RecursoHumano', 'Actividad', 'LanguageModel']
```

### ¿Que es eso de model y controler?
Model tiene todas las funciones necesarias para manejar la tabla.
Controler usa las funciones de model de manera segura. Aprueba de errores. El controler es el que usara el app.

Modelo = Trabajador especializado (sabe EXACTAMENTE cómo hablar con la BD)
Controlador = Gerente (coordina, valida, y decide CUÁNDO usar al trabajador)

Logica de nombres de programación:
- Modulos snake_case: modulo_chido.py
- Clases como PascalCase: NombreDeClases
- Metodos/funciones como snake_case: metodo_potente
- Variables como snake_case: nombre_variable




## Arbol del proyecto
```bash
data/
    administradorDeActividad.db
    
    # Restructurar language.py a: language_model.py, language_controller.py, language_service.py
    # model funciones para manejar la db. controler manejar model de manera segura. 
    # service unificar model y controler
    language.db
    language.py

models/
    __init__.py
    database.py         # Conexión y creación de tablas
    tarea_model.py      # Modelo para tabla tarea
    recurso_model.py    # Modelo para tabla recurso humna
    actividad_model.py  # Modelo para tabla actividad

controllers/
    __init__.py
    tarea_controller.py
    recurso_controller.py
    actividad_controller.py

views/
    __init__.py
    qt_app/
        # Aplicacion
        main_window.py
    interface/
        # Modulos relacionados con la interfaz
        qt/
            Modulo_Util_Qt.py
        interface_number.py
        css_util.py

core/
    # Funciones logicas para uso general
    config/
        System_data.py
    
    display_number.py
    Modulo_Files.py
    Modulo_Text.py
    Modulo_System.py

config/
    # Archivos de texto con info para programas.
    Terminal_Run.dat

resources/
    __init__.py
    interface_info.py # Mejor que sea algo mas general. Como paths.py, Con la ruta de todo lo que este aca.
    images/

main.py
requirements.txt # Dependencias
```