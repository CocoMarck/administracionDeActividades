# Documentar  
*Documentación relacionada con la programación*  
Aprender a documentar el programa/proyecto de manera estructurada y estandarizada.

Se puede documentar el programa con puros comentarios, de hecho así se empieza a documentar un programa. Pero una vez completado el programa, es muy bueno crear textos informativos. Recomiendo mucho usar `Markdown`, un lenguaje de mercado chidori.

Yo personalmente paso de `md to html to pdf`, aveces lo paso de `html to odt to pdf`, ya que con el `odt` puedo hacer retoques en LibreOffice. Puedes probar en Microsoft Office, siendo de paga seguro abre `HTML`.




# ¿Que documentar?
Basicamente se tienen que hacer textos por cada parte importante del proyecto. Por ejemplo, el modulo `wakanda_forever.py`, se usa mucho en modulos de `models`. Bueno, entonces es buena idea darle una documentación detallada a este modulo. Especialmente si sus metodos no cambiaran mucho. Es decir puede que tengas que factorizar el código, pero los `return` devolveran lo mismo.




# Prioridades en documentación
Mas que nada las *partes del programa mas usadas y stables*, porque puede que `testing_cocos.py` este en progreso y algunos de sus metodos incluso dejen de existir. Elige bien que documentar, esto te ayudara a evitar perdidas de tiempo.

### Ejemplo de prioridades:
- Modulos estables terminados.
- Programa/Proyecto/App terminada. Documentar especificamente las funcionalidades del programa terminado.
- Modulos inestables en uso; pero bien definidas sus funciones
- Modulos en pruebas; sus funciones aun no estan completamente definidas.

> Yo personalmente prioririso documentar primero partes del programa terminadas, antes que el programa completo, ya que el programa terminado, suele ser intuitivo, y puedo no necesitar tanto la documentación. Realmente esto depende de como sea tu programa. Capaz si es un videojuego, pues no necesita tanto de una documentación el videojuego en si, pero sus `modulos/partes` 100% seguro que si.