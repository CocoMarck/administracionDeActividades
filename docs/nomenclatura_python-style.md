# Nomenclatura python style
Los lenguajes de programación varian un poco en como su *estandar* de nombres para todo; variables, funciones, archivos, clases, y etc. Aca veremos como nombrar todo, estilo `python`.




# Entender los tipos de datos, tambien los objetos y funciones
Esto es importante, porque es necesario entender que es una `variable` que es una `CONSTANTE`, que es una `funcion`, que es un `Objeto`. Incluso es importante saber que es un `archivo`, que es una `carpeta`.

Cosas que en si son sencillas de aprender, pero es bueno darle una pasada para fortalecer conocimientos.

> Programando mucho, lo vas a tener claro como el water.




# Logica de nombres de programación en python *(Entre otros)*
La regla [PEP 8](https://peps.python.org/pep-0008/) indica como estilizar tu código python.
- Modulos/Carpetas snake_case: `modulo_chido.py`
- `Clases/Objetos` como PascalCase: `NombreDeClases`
- Metodos/funciones como snake_case: `metodo_potente`
- Variables/Parametros como snake_case: `nombre_variable`
- Constantes snake_case en mayucuslas: `NOMBRE_CONSTANTE`



# Los nombres privados
Estos no son nombres groseros, o de mal gusto, sino que son nombres que tienen intención de solo verse em in `metodo` o en una `Clase`. Son nombres que se ocultan por convención, se acceden a ellos de una manera distinta a los datos `publicos/normales`. De hecho se recomienda no tocarlos *(se podria romper algo)*. Uno pone datos privados porque quiere que no se toquen, ya que debido a como jala el programa, si se manipulan de manera indevida, algo se puede romper.