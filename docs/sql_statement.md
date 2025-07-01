# Instrucciones SQLite3
Aca se veran algunos ejemplos de intrucciones sql, generalmente, seran instrucciones complejas.

> SQLite, no diferencia de mayusculas, puedes secribir las palabras reservadas como se te de la gana.


### Query para llenar la tabla llamada actividad (Join con dos tablas)
```sql
Select a.ActividadId, a.TareaId, b.Nombre, a.NOTA, a.FechaInicio, a.FechaFin, a.Horas, a.Baja
  From Actividad a
 Inner Join RECURSOHUMANO b on a.RecursoHumanoId = b.RecursoHumanoId
 where a.Baja = 0 and b.Baja = 0
```
Aca `actividad` tiene el alias `a`, y la tabla `recursohumano` tiene el alias `b`.

### Query para llenar la tabla llamada actividad (Join con tres tablas)
```sql
Select a.ActividadId, a.TareaId, c.Descripcion, b.Nombre, a.NOTA, a.FechaInicio, a.FechaFin, a.Horas, a.Baja
  From Actividad a
 Inner Join RECURSOHUMANO b on a.RecursoHumanoId = b.RecursoHumanoId
 Inner Join Tarea          c on a.TareaId = c.TareaId
 where a.Baja = 0 and b.Baja = 0 and c.Baja = 0
```
Aca `actividad` tiene el alias `a`, la tabla `recursohumano` tiene el alias `b`, y la tabla `tarea` tiene el alias `c`.