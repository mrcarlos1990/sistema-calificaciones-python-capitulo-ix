# Sistema de Control de Calificaciones - Capítulo IX

**Estudiante:** Amauri Feliz Valenzuela · **Institución:** Instituto Tecnológico de Las Américas (ITLA).
**Asignatura:** Introducción a la Programación · **Profesor:** Jimmy Gómez.
**Modalidad:** individual · **Fecha:** 10 de octubre de 2026 · **Lenguaje:** Python.

Aplicación de consola para administrar las notas de cinco estudiantes mediante dos listas relacionadas. Su objetivo es practicar vectores, índices, ciclos, condiciones, cálculos y validación con código sencillo.

**Procedencia de los datos:** Ana, Luis, Carlos, Maria y Pedro, con notas 85, 67, 92, 74 y 58, son el conjunto de ejemplo fijado en el enunciado de la asignación. Los registros muestran pruebas de ese ejercicio y cambios de demostración; no provienen de una consulta a expedientes académicos ni de una base de datos de estudiantes.

## Funcionalidades

- Mostrar nombres y calificaciones; consultar por índice.
- Calcular promedio, máximo y mínimo.
- Mostrar y contar aprobados y reprobados.
- Modificar notas, buscar nombres y mostrar un resumen actualizado.
- Validar enteros, índices, opciones y notas fuera del rango; salir con opción 0.

La escala es de 0 a 100, con notas enteras. Aprobar requiere 70 puntos: es una regla del proyecto, no una afirmación sobre la política académica del ITLA. Los cambios se conservan durante la sesión; al reiniciar se recuperan los datos iniciales.

## Requisitos e instalación en Windows

1. Instalar Python 3 y Visual Studio Code. Git es necesario solamente para versionar o subir el proyecto.
2. Descargar los archivos o copiar esta carpeta a una ubicación propia. No se necesitan bibliotecas externas para ejecutar el programa ni las pruebas.
3. En VS Code, seleccionar **Archivo > Abrir carpeta** y abrir esta carpeta.
4. Abrir **Terminal > Nueva terminal**, verificar `py --version` y ejecutar:

```powershell
py main.py
```

Si `py` no está disponible y Python está en PATH, utilizar `python main.py`. El programa pide una opción; escribir el número y pulsar Enter.

## Ejemplos de uso

- `1`: Ana 85, Luis 67, Carlos 92, Maria 74 y Pedro 58.
- `2`, luego `2`: Carlos tiene 92 puntos.
- `3`: promedio 75.20, porque 376 / 5 = 75.2.
- `8`, luego `1` y `80`: Luis cambia de 67 a 80. Con `1` se verifica la lista actualizada y con `3` el promedio pasa a 77.80.
- `9`, luego `luis`: encuentra a Luis sin distinguir mayúsculas. Escribir `Maria` como aparece en los datos; la búsqueda no elimina tildes.
- `0`: finaliza correctamente.

## Arreglos y vectores

Las listas representan vectores unidimensionales en este ejercicio:

```python
estudiantes = ["Ana", "Luis", "Carlos", "Maria", "Pedro"]
calificaciones = [85, 67, 92, 74, 58]
```

El índice 0 corresponde a Ana y a 85. Hay cinco elementos; el último índice es 4. Mantener la misma longitud y orden evita asignar una nota a otro estudiante. No se ordena una lista de forma independiente. Una lista de Python es dinámica y puede contener tipos distintos; no es idéntica a un arreglo fijo y homogéneo de otros lenguajes.

## Pruebas reproducibles

```powershell
py -m unittest discover -s pruebas -v
```

Un método de prueba ejecuta nueve sesiones independientes de `main.py`, con sus datos iniciales restaurados. Comprueba resultados, salida normal y ausencia de errores. Las pruebas generan `evidencias/ejecucion_01.txt` a `ejecucion_09.txt` y `resultados.json`. El código de las pruebas emplea herramientas estándar para automatizar la comprobación; esas herramientas no forman parte de la lógica que se estudia en `main.py`.

## Evidencias disponibles

Se conservan nueve transcripciones auténticas de procesos ejecutados y sus resultados estructurados. **No son capturas de pantalla.** Las siete figuras solicitadas quedan pendientes por falta de acceso a la interfaz nativa. Consultar `evidencias/GUIA_CAPTURAS.md` para obtenerlas. No hay imágenes falsas ni archivos vacíos.

## Documentación

- `documentacion/Amauri_Feliz_Actividad_Arreglos.pdf`: investigación, desarrollo, siete componentes explicados, pruebas, fuentes y pendientes.
- `documentacion/investigacion.md`: texto editable de la investigación.
- `documentacion/GUIA_DEFENSA.md`: respuestas breves para la evaluación.
- `documentacion/AUDITORIA.md`: cumplimiento y limitaciones.

## GitHub y publicación

Repositorio público creado y verificado en la cuenta `mrcarlos1990`, con autorización expresa del estudiante:

[sistema-calificaciones-python-capitulo-ix](https://github.com/mrcarlos1990/sistema-calificaciones-python-capitulo-ix)

El código completo, las pruebas, sus transcripciones y el PDF se publican en este repositorio. Las siete capturas de Visual Studio Code siguen pendientes; el PDF está identificado como versión para revisión hasta incorporarlas y verificarlo de nuevo.

Para publicarlo manualmente después de revisar:

1. Iniciar sesión en GitHub, seleccionar **New repository**, nombre `sistema-calificaciones-python-capitulo-ix`.
2. Elegir visibilidad conscientemente: el documento contiene nombre e información académica. No inicializar el remoto con README si se enviará la carpeta completa con Git.
3. Desde la terminal de esta carpeta:

```powershell
git init
git add main.py README.md .gitignore .gitattributes pruebas evidencias documentacion
git commit -m "Agrega proyecto académico de arreglos y vectores"
git branch -M main
```

4. Copiar la URL real que GitHub muestre y ejecutar `git remote add origin URL_REAL_COPIADA`, sustituyendo ese marcador. Ejecutar `git push -u origin main` y autenticarse si se solicita.
5. Abrir el repositorio y verificar el código, las evidencias y el PDF. Agregar el enlace comprobado a este README y a la investigación, regenerar el PDF y subir la actualización.

Alternativa sin Git: en el repositorio, **Add file > Upload files**, subir los archivos y carpetas de esta asignación y confirmar el envío. No subir archivos del proyecto de préstamos que contiene esta carpeta.

## Fuentes

Python Software Foundation, documentación oficial, consulta del 10 de octubre de 2026:

- [Introducción informal: listas e indexación](https://docs.python.org/es/3/tutorial/introduction.html).
- [Estructuras de datos](https://docs.python.org/es/3/tutorial/datastructures.html).
- [Herramientas para control de flujo](https://docs.python.org/es/3/tutorial/controlflow.html).
