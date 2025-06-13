# Administración de actividades

Administra las diferentes actividades realizadas por los usuarios, en base a tareas predefinidas.
Programa hecho con python3 y SQLite3. Nombre del repo: administracionDeActividades


# Tablas
## TAREA
| Columna               |  Valor     | Default |
|-----------------------|------------|---------|
| TareaId               |  INT AUTO  | NULL    |
| Descripcion           |  VARCHAR   | NULL    |
| UsuarioCreacionId     |  INT       | NULL    |
| FechaCreacion         |  DATETIME  |         |
| UsuarioModificacionId |  INT       | NULL    |
| FechaModificacion     |  DATETIME  | NULL    |
| UsuarioBajaId         |  INT       | NULL    |
| FechaBaja             |  DATETIME  | NULL    |
| Baja                  |  BIT       | 0       |


Campos de control: UsuarioCreacionId, FechaCreacion, UsuarioModificacionId, FechaModificacion, UsuarioBajaId, FechaBaja, Baja

Los campos de control los tendran todas las tablas.


## RECURSO HUMANO
| Columna          | Valor       |
|------------------|-------------|
| RecursoHumanoId  | INT AUTO    |
| Numbre           | VARCHAR(40) |
| APP              | VARCHAR(40) |
| APM              | VARCHAR(40) |
| Puesto           | VARCHAR(40) |



## ACTIVIDAD
| Columna        |  Valor     | Default  |
|----------------|------------|----------|
| ActividadId    |  INT       | AUTO     |
| TareaId        |  INT       | NOT NULL |
| RecursoHumanoId |  INT       | NOT NULL |
| NOTA           |  TEXT      | NULL     |
| FechaInicio    |  DATETIME  | NOT NULL |
| FechaFin       |  DATETIME  | NOT NULL |
| HORAS          |  DECIMAL   | Calculado|
| RecursoHumanoId|  INT       |          |




# Probar programa
> Este programa se creo en Debian 12, pero deberia funcionar en windows.

### En GNU/Linux Debian:
```bash
python3 ./main.py
```

### En Windows:
```shell
py .\main.py
```