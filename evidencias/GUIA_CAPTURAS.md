# Capturas auténticas pendientes

## Preparación en Visual Studio Code

1. Abre VS Code y selecciona **Archivo > Abrir carpeta**. Elige solamente la carpeta `sistema-calificaciones-python-capitulo-ix` que está dentro del proyecto actual. Evita abrir la carpeta general del sistema de préstamos.
2. Abre `main.py` desde el explorador izquierdo. Maximiza VS Code y cierra pestañas ajenas a la asignación.
3. Usa **Ver > Apariencia > Acercar** hasta que el código se lea cómodamente. Puedes ocultar la barra lateral con **Ver > Apariencia > Barra lateral principal** cuando necesites más espacio.
4. Abre **Terminal > Nueva terminal**. Comprueba que la terminal esté ubicada en esta carpeta. Escribe `py --version`. Si no reconoce `py`, prueba `python --version`; usa el comando que funcione en los pasos siguientes. Si ninguno funciona, instala Python desde su sitio oficial antes de continuar.
5. Escribe `py main.py` y pulsa Enter. No ejecutes otros archivos del proyecto de préstamos.
6. Para guardar cada captura, pulsa **Win + Shift + S**, selecciona captura de ventana o una región que incluya el título de VS Code y el contenido relevante. Abre la notificación de Recortes y elige **Guardar como**, formato PNG.
7. Guarda cada imagen dentro de `evidencias` con el nombre exacto indicado abajo. No captures credenciales, correos, otras ventanas ni archivos privados. Conserva los mensajes relevantes y suficiente contexto para reconocer la ejecución; no recortes errores para ocultarlos.

No uses capturas del PDF ni imágenes de transcripciones como sustituto de las capturas de VS Code. No agregues notas dibujadas encima de los resultados ni cambies las salidas. Los títulos y explicaciones se incorporarán fuera de la imagen en el PDF.

## Secuencia de las siete figuras

### Captura 1: código fuente

1. Selecciona la pestaña `main.py` y oculta la terminal si ocupa demasiado espacio.
2. Ve al comienzo del archivo con Ctrl + Inicio. Muestra el nombre del archivo, `MINIMO_APROBACION`, `leer_entero` y parte de las funciones siguientes con texto legible.
3. Guarda como `captura_01.png`. No hace falta mostrar todo el archivo en una sola imagen: el código íntegro estará en el repositorio.

### Captura 2: vectores iniciales

1. Dentro de `main.py`, busca `def main():` con Ctrl + F y cierra la búsqueda.
2. Muestra claramente `estudiantes` y `calificaciones`, incluyendo los cinco valores de cada lista y el comentario de correspondencia.
3. Guarda como `captura_02.png`.

### Captura 3: menú principal

1. Abre la terminal integrada. Inicia una sesión nueva con `py main.py`.
2. Antes de introducir una opción, muestra el menú completo de 1 a 10 y 0, junto con **Seleccione una opción**.
3. Puedes ampliar el panel terminal arrastrando su borde superior o usar **Maximizar tamaño del panel** desde el menú del panel.
4. Guarda como `captura_03.png`.

### Captura 4: resultados académicos

1. En esa sesión nueva, escribe `10` y pulsa Enter. No modifiques notas todavía.
2. Desplázate dentro de la terminal para mostrar el resumen con los cinco estudiantes, **Promedio general: 75.20**, **Calificación más alta: 92** y **Calificación más baja: 58**.
3. Si cabe, incluye también tres aprobados y dos reprobados. Ajusta el tamaño del panel sin volver ilegible el texto.
4. Guarda como `captura_04.png`.

### Captura 5: modificación

1. Escribe `8` y pulsa Enter.
2. Cuando pida índice, escribe `1` y pulsa Enter.
3. Cuando pida la nueva nota, escribe `80` y pulsa Enter.
4. Comprueba **Luis: antes 67, ahora 80 puntos**. Escribe `1` para mostrar la lista actualizada.
5. Muestra el mensaje antes/después y el listado con **1. Luis: 80 puntos**. Si el menú separa ambos resultados, amplía el panel y desplázate hasta incluirlos sin ocultar los mensajes intermedios relevantes.
6. Guarda como `captura_05.png`.

### Captura 6: validación

1. Escribe `2` y pulsa Enter para consultar por índice.
2. Introduce `9` y pulsa Enter. Debe aparecer **Valor fuera de rango: debe estar entre 0 y 4**.
3. Introduce ahora `2` y pulsa Enter. Debe aparecer **Carlos: 92 puntos**.
4. Muestra la entrada incorrecta, el aviso y la consulta corregida, que demuestra continuidad.
5. Guarda como `captura_06.png`.

### Captura 7: finalización

1. En el menú escribe `0` y pulsa Enter.
2. Muestra la opción de salida, **Programa finalizado correctamente** y el retorno al indicador de la terminal de VS Code.
3. Guarda como `captura_07.png`.

## Entrega y verificación

Al terminar, avisa en el chat: **Ya guardé las siete capturas en evidencias**. Si no puedes guardarlas en esa carpeta, adjunta las siete imágenes reales directamente en el chat. No envíes contraseñas ni códigos de GitHub.

Se revisará cada imagen para confirmar que corresponde al archivo y a los resultados descritos, que es legible y que no incluye datos privados. Después se incorporarán al PDF con los títulos y explicaciones de abajo, se regenerará el índice y se revisarán todas las páginas. El PDF seguirá marcado como pendiente mientras falte alguna figura o evidencia no sea verificable.

## Títulos y explicaciones para el documento

Las transcripciones TXT disponibles provienen de ejecuciones reales. No reemplazan las capturas pedidas. Para obtener imágenes auténticas en Windows, abrir únicamente esta carpeta en VS Code, aumentar el tamaño del texto y utilizar Win + Shift + S. Incluir suficiente contexto para que se reconozca la aplicación, sin ocultar mensajes relevantes. Revisar que no se vean credenciales, correos ni archivos ajenos.

1. **Figura 1. Código fuente del programa.** Abrir `main.py` en VS Code y guardar `captura_01.png`. Explicación: archivo principal y funciones que organizan el sistema.
2. **Figura 2. Vectores iniciales.** Mostrar las dos listas dentro de `main()`, guardar `captura_02.png`. Explicación: un mismo índice relaciona cada nombre con su nota.
3. **Figura 3. Menú principal.** Ejecutar `py main.py`, guardar `captura_03.png`. Explicación: el menú permite seleccionar operaciones y se repite hasta salir.
4. **Figura 4. Resultados académicos.** En una sesión nueva elegir 10; guardar `captura_04.png` mostrando promedio 75.20, máximo 92 y mínimo 58. Explicación: cálculos realizados con los cinco valores iniciales.
5. **Figura 5. Modificación de una calificación.** Elegir 8, índice 1 y nota 80; luego 1. Guardar `captura_05.png` con el mensaje antes 67 / ahora 80 y la lista actualizada. Explicación: se sustituye el elemento del índice 1.
6. **Figura 6. Validación del programa.** Elegir 2, introducir 9 y después 2. Guardar `captura_06.png` con el aviso y Carlos 92. Explicación: un índice inválido se rechaza y se permite corregirlo.
7. **Figura 7. Ejecución final.** Seleccionar 0 y guardar `captura_07.png`. Explicación: el ciclo termina con un mensaje de cierre correcto.

No afirmar que se tomaron estas capturas hasta que existan. Tras incorporarlas, añadir título, explicación e imagen al PDF; revisar de nuevo su legibilidad y actualizar la auditoría.
