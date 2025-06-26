# Tabla Actividad

# Crear funcion para obtener solo los datos para vista.
La instrucción se llamara `get_values_for_the_view`
Junto con la función: `get_columns_for_the_view`

### Columnas vista:
Id, Texto de TareaId y RecursoHumanoId,


# Rango de fechas. Para el query con filtros.
### Con BETWEEN
```sql
a.FechaInicio BETWEEN '0000-00-00T00:00:00' and '0000-00-00T00:00:00'
```

### Con operador >=
```sql
a.FechaInicio >= '0000-00-00T00:00:00' and a.FechaFin <= '0000-00-00T00:00:00'
```