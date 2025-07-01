# Nombres para base de datos
Usar estándar (`PEP8`, estilo `Python/PascalCase` para clases).

Para snake_case: `database`
Para PascalCase: `Database`
para camelCase: `database`

### Para las clases siempre se usa `PascalCase`
Para un model database. `StandardDatabase`, para su controller `StandardDatabaseController`

---




# Usar snake case casi todo
Para las var y funcs, solo usar snake_case:
```
var = bool

def good_state():
    ....
```

---




# Mayusculas + snake case para constantes
Para las constantes, no importa su tipo de valor, sus nombres son en mayusculas y `snake_case`:
```
CONSTANTE = str

CONSTANTE_DE_ALTO_RENDIMIENTO = str
```