'''
Este modulo es para información numerica relacionada con la interfaz.
Por ejemplo:
Valores xy de dimenciónes de ventana.
Valores xy de para fuente de texto.
Valores xy de para iconos.
'''
from core.display_number import *


# Establecer dimenciones de windegts y ventana
# Limite de resolucion: Anchura y altura de 480px como minimo.
num_font = get_display_number(divisor=120)
num_space_padding = num_font//4
num_margin_xy = [num_font//2, num_font//4]

nums_win_main = [
    get_display_number(multipler=0.8, based='width'),
    get_display_number(multipler=0.8, based='height')
]