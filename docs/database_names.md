# Modulo para establecer nombres relacionados con la base de datos.
Nombre de base de datos, nombre de tablas, nombre de columnas.
Usar nombres, en los `models`, y `controllers` de la base de datos relacionada. Tanto los `db` como los `tables`

Este modulo se llamara, `database_names.py` y estara en la carpeta: `models`

> Estara en `models`, porque esta relacionado unicamente con la base de datos.

Los nompres a pesar de ser usado para `nombre.db`, o con cualquier extención, no se pondran con extención, solo `nombre`. La extención sera puesta en otro lado, generalmente en en `model` del `database`.

Es necesario establecer de dichas nombres de variables, en mayusculas, debido a que estas son constantes.


# Constantes, diccionarios
Habra constantes, pero lo que se usaran son los diccionarios, con los nombres.


## Nomenclatura de keys
Seran textos en minusculas, sin espacios, lo que se podra usar como espacio seran guion `-` y guion bajo `_`.

~~~
"nombres-de-key_parte1"
~~~


# ¿Que nombres contendra?
```python
TABLE_CONTROL_FIELDS = {
    "usercreationid":       "UsuarioCreacionId",
    "creationdate":         "FechaCreacion",
    "usermodificationid":   "UsuarioModificacionId",
    "modificationdate":     "FechaModificacion",
    "userlowid":            "UsuarioBajaId",
    "lowdate":              "FechaBaja",
    "low":                  "Baja"
}
```

### Es posible que sea adecuado hacer un entity. Pero la verdad ni se me ocurre como, es posible que no lo necesite, pero puede que si, es bueno recordarlo.