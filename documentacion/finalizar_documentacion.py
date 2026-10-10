"""Prepara la documentación local después de revisar las siete capturas."""
import hashlib
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
figuras_path = RAIZ / "evidencias/figuras.json"
figuras = json.loads(figuras_path.read_text(encoding="utf-8"))
explicaciones = [
    "Presento main.py abierto en Visual Studio Code. La función leer_entero valida las entradas y el ciclo for permite mostrar las calificaciones.",
    "Utilizo dos listas de cinco elementos. Relaciono cada nombre con su nota mediante el mismo índice; por ejemplo, Ana ocupa la posición 0 y tiene 85 puntos.",
    "Inicio el programa desde la terminal integrada de Visual Studio Code. El menú ofrece diez operaciones y la opción 0 para salir.",
    "Consulto el resumen con los datos iniciales. Obtengo un promedio de 75.20, una nota máxima de 92 y una mínima de 58; hay tres aprobados y dos reprobados.",
    "Selecciono la opción 8, el índice 1 y la nota 80. El mensaje confirma que la calificación de Luis cambió de 67 a 80 puntos y el menú continúa disponible.",
    "Introduzco el índice 9 y el programa lo rechaza. Al corregirlo a 2, consulto a Carlos con 92 puntos; la validación permite continuar sin cerrar el sistema.",
    "Selecciono la opción 0. El mensaje Programa finalizado correctamente y el regreso a la terminal muestran que el ciclo del menú terminó de forma normal.",
]
for i, figura in enumerate(figuras):
    ruta = RAIZ / "evidencias" / figura["archivo"]
    assert ruta.is_file()
    figura.update(revisada=True, sha256=hashlib.sha256(ruta.read_bytes()).hexdigest(), explicacion=explicaciones[i])
figuras_path.write_text(json.dumps(figuras, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

p = RAIZ / "documentacion/investigacion.md"
s = p.read_text(encoding="utf-8")
s = s.replace("Visual Studio Code es el entorno solicitado para abrir y explicar el proyecto; no se afirma que haya sido utilizado durante las ejecuciones registradas. Las capturas de su interfaz siguen pendientes.", "Las siete capturas aportadas por el estudiante muestran además el código y la ejecución manual en Visual Studio Code. Las pruebas automatizadas y las capturas constituyen evidencias distintas y sus resultados coinciden.")
s = s.replace("Visual Studio Code es el editor previsto para revisarlo en clase.", "Visual Studio Code es el editor utilizado para las capturas del código y la terminal integrada.")
s = s.replace("El acceso al perfil de GitHub se comprobó, pero el proyecto no se ha publicado. No se atribuye al estudiante el uso de herramientas que todavía debe revisar o ejecutar personalmente.", "El repositorio público de GitHub se publicó y su acceso se verificó sin credenciales. Las capturas documentan la ejecución realizada por el estudiante.")
s = s.replace("Se publican el código completo, las pruebas, las transcripciones y la documentación. Las siete capturas auténticas de Visual Studio Code todavía deben obtenerse, revisarse e incorporarse. Por esa razón, el PDF continúa como versión para revisión y no se declara terminado el requisito de evidencias gráficas.", "El repositorio contiene el código completo, las pruebas, las transcripciones y la documentación anterior. Esta versión local incorpora las siete capturas revisadas. Su actualización en GitHub queda preparada y se publicará únicamente después de la autorización del estudiante.")
s = s.replace("Las figuras 1 a 7 quedan pendientes: código abierto en VS Code, vectores iniciales, menú, resultados académicos, modificación, validación y cierre. GUIA_CAPTURAS.md describe cómo obtener cada una en Windows e incluye el título y la explicación que deben acompañarla. La herramienta disponible no permite acceder a las aplicaciones nativas para tomarlas.", "Las figuras 1 a 7 muestran, en orden, el código abierto en VS Code, los vectores iniciales, el menú, los resultados académicos, la modificación, la validación y el cierre. Las imágenes originales se conservan completas; las páginas horizontales facilitan la lectura. Los mensajes Unknown word visibles en el editor corresponden al corrector ortográfico que marca palabras españolas, no a errores de ejecución. Las indicaciones de tipo atenuadas son ayudas visuales del editor y no cambian el código fuente.")
s = s.replace("No se documentan dificultades personales del estudiante porque no fueron confirmadas. Durante la preparación se detectó una limitación verificable del entorno: no hay control de la interfaz nativa para capturar VS Code y la terminal. La solución disponible consiste en conservar las salidas reales y facilitar una guía para tomar las imágenes manualmente.", "No se atribuyen dificultades personales al estudiante sin su confirmación. Para completar las evidencias se preparó una guía de captura y el estudiante aportó las siete imágenes reales de Visual Studio Code. Los avisos del corrector ortográfico visibles en el editor se distinguen de los resultados de ejecución, que se comprobaron nuevamente mediante las pruebas.")
p.write_text(s, encoding="utf-8", newline="\n")

p = RAIZ / "README.md"
s = p.read_text(encoding="utf-8")
s = s.replace("Las siete figuras solicitadas quedan pendientes por falta de acceso a la interfaz nativa. Consultar `evidencias/GUIA_CAPTURAS.md` para obtenerlas. No hay imágenes falsas ni archivos vacíos.", "Las siete capturas auténticas aportadas por el estudiante se revisaron y se incorporaron al PDF con sus títulos y explicaciones. Están en `evidencias/captura_01.png` a `captura_07.png`. Los originales se conservan completos. Los avisos Unknown word corresponden al corrector ortográfico del editor, no a errores del programa.")
s = s.replace("pruebas, fuentes y pendientes.", "pruebas, siete capturas y fuentes.")
s = s.replace("Las siete capturas de Visual Studio Code siguen pendientes; el PDF está identificado como versión para revisión hasta incorporarlas y verificarlo de nuevo.", "El PDF local definitivo incorpora las siete capturas de Visual Studio Code. La actualización pública de estas imágenes y del documento requiere la autorización final del estudiante.")
p.write_text(s, encoding="utf-8", newline="\n")
print("Siete capturas revisadas registradas; investigación y README actualizados localmente.")
