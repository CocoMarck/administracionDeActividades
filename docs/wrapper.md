# Wrappers
Son fachadas para un programa/modulo.

Sirve para usar el programa/modulo complejo de manera mas directa o bonita.

Haz de cuenta tienes este modulo:
`from controllers import TextController`
```
class TextController:
    def get_text(self, key: str) -> tuple:
        if key == "saludo":
            return "Hola", "INFO", "Texto encontrado"
        else:
            return "", "ERROR", f"No se encontró el texto: {key}"
```
Su funcion devuelve tres datos. Conveniente para mostrar mensajes o alguna otra cosa. Pero ineficiente para el uso general.

### Ejemplo de uso:
```
print( controller.get_text("saludo") )
```
Resultado: `("Hola", "INFO", "Texto encontrado")`

Yo solo queria obtener el hola, no esos tres datos.




## Con el wrapper
```python
from controllers import TextController

controller = TextController()

def get_text(key: str) -> str:
    value, _, _ = controller.get_text(key)
    return value
```

### Ejemplo de uso
```
```
`from util.text_loader import get_text`
```python
get_text("saludo")
```
Resultado: `"Hola"`





# ¿Donde se pued guardar el wraper?
- `utils/wrapper_name.py`
- `utils/wrappers/wrapper_name.py`