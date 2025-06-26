### 2025-24-06 21:10

# Pestaña Consulta Actividad

### Query para el filtro de Consultar Actividad

```sql
Select * from Actividad where FechaInicio >= '2025-06-17T00:45:00' and fechaFin <= '2025-06-31T20:22:27'
```

### Como obtener el numero del último día del mes en Pytho

```python
import calendar
import datetime

def ultimo_dia_mes_actual():
  """Obtiene el último día del mes actual."""
  hoy = datetime.date.today()
  _, numero_dias = calendar.monthrange(hoy.year, hoy.month)
  return numero_dias

# Ejemplo de uso:
ultimo_dia = ultimo_dia_mes_actual()
print(f"El último día del mes actual es: {ultimo_dia}")
```

### Correcciones a la pestaña ActividadQuery
1. Que cuando de click a la pestaña carge la tabla con todos los registros del mes que corresponde a la fecha inicio
2. En quitar filtro que la tabla se carge con los datos siguiendo los criterios del punto 1.
3. Quitar el boton Cancelar
4. Que tanto en fecha inicio como en fecha fin se muestre la fecha en horario militar y con los segundos
5. Por default (cuando entre a la pestaña Consultar) la fecha inicio corresponde al primer día del mes en curso y la fecha fin corresponde al último día del mismo mes en curso
6. Cambiar el nombre de la pestaña ActividadQuery a Consultar
7. Cambiar el texto al botón `Actualizar datos` y poner el texto `Filtro default`


### Otra corrección
1. En todas las pestañas, que las funciones de los botones Agregar y Actualizar se lleven acabo con un solo botón llamado: Guradar