
---
`2025-06-24 21:10`
---

# Pestaña Consulta Actividad

# Query para el filtro de Consultar Actividad
### LISTO
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




# Correcciones a la pestaña ActividadQuery
### LISTO

1. Que cuando de click a la pestaña carge la tabla con todos los registros del mes que corresponde a la fecha inicio
2. En quitar filtro que la tabla se carge con los datos siguiendo los criterios del punto 1.
3. Quitar el boton Cancelar
4. Que tanto en fecha inicio como en fecha fin se muestre la fecha en horario militar y con los segundos
5. Por default (cuando entre a la pestaña Consultar) la fecha inicio corresponde al primer día del mes en curso y la fecha fin corresponde al último día del mismo mes en curso
6. Cambiar el nombre de la pestaña ActividadQuery a Consultar
7. Cambiar el texto al botón `Actualizar datos` y poner el texto `Filtro default`





# Otra corrección
### LISTO
1. En todas las pestañas, que las funciones de los botones Agregar y Actualizar se lleven acabo con un solo botón llamado: Guradar

---
`2025-06-26 18:03`
---




# Pestaña ActividadQuery

1. Cambiar el nombre de esta pestaña por **Consulta Actividad**
2. Que al dar click en la pestaña `Consulta Actividad` la consulta que se muestra sea la correspondiente a la del mes en curso
3. Que al dar click en el boton `Filtro por defecto` se muestre la consulta como en el punto numero 2.
4. Que en la fecha inicio y fecha fin los segundos siempre sean `:00`
5. Poner longitud fija a las columnas de la tabla en todas las pestañas


```python

''' Para obtener el mes actual en Python, puedes utilizar el módulo datetime. Primero, 
    importa el módulo datetime y luego utiliza datetime.now().month para obtener el número 
    del mes actual (1 para enero, 2 para febrero, etc.). 
'''

import datetime

mes_actual = datetime.datetime.now().month
print(mes_actual)

# Si necesitas el nombre del mes, puedes usar strftime con el formato %B (nombre completo del mes) o %b (nombre abreviado). 

import datetime

nombre_mes_completo = datetime.datetime.now().strftime("%B")
nombre_mes_abreviado = datetime.datetime.now().strftime("%b")

print(f"Mes completo: {nombre_mes_completo}")
print(f"Mes abreviado: {nombre_mes_abreviado}")

```