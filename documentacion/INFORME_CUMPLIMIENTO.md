# Informe de cumplimiento — Capítulo IX: Arreglos y Vectores

Fecha: 10 de octubre de 2026. Estudiante: Amauri Feliz Valenzuela. Matrícula: 201631629. Profesor: Jimmy Gómez.

Base de la auditoría: mandato completo facilitado por el estudiante en este chat. Se revisó cada requisito contra archivos locales, ejecuciones reales, documento renderizado y acceso público a GitHub.

**Estado académico y del PDF: LISTO PARA ENTREGAR.** No hay requisitos académicos obligatorios pendientes. La publicación de esta revisión en GitHub sigue sin realizarse porque requiere autorización expresa; el mandato exige acceso al código completo y README, que ya están publicados y verificados.

Documento de entrega: `ENTREGA_FINAL/Amauri_Feliz_Actividad_Arreglos.pdf` (18 páginas). Original conservado en `documentacion/Amauri_Feliz_Actividad_Arreglos.pdf`.

## Identificación y portada

| Requisito | Estado | Comprobación |
| --- | --- | --- |
| Institución, asignatura, capítulo, título y fecha correctos | CUMPLE | Portada, p. 1; encabezados y fecha 10-10-2026. |
| Nombre, matrícula, grupo y profesor correctos | CUMPLE | Portada: Amauri Feliz Valenzuela; 201631629; PRG-101-C-2026-03-JG; Jimmy Gómez. |
| Trabajo individual e investigación con desarrollo práctico | CUMPLE | Introducción y objetivos; autor único en portada y metadatos; README. |
| Conservar exactamente portada, logo, colores y decoración | CUMPLE | Contenido de la página 1 idéntico al original; comparación de renderizados sin diferencias de píxeles. |
| Una portada y contenido desde la segunda página | CUMPLE | P. 1 portada; p. 2 índice; p. 3 introducción. No existe otra portada. |

## Parte I — Investigación y conceptos

| Requisito | Estado | Comprobación |
| --- | --- | --- |
| Definir arreglo y explicar para qué se utiliza | CUMPLE | 9.1, p. 3: colección accesible por posición; calificaciones, nombres y temperaturas. |
| Ventajas frente a variables independientes | CUMPLE | 9.1, p. 3: organizar datos y repetir operaciones mediante un recorrido. |
| Información almacenada | CUMPLE | 9.1: enteros, texto y valores lógicos; dos listas separadas en el proyecto. |
| Diferencia entre variable individual y arreglo | CUMPLE | 9.1: nota = 85 frente a una lista con cinco valores. |
| Ejemplo calificaciones = [85, 90, 78, 95, 88] | CUMPLE | 9.1: código exacto; cinco enteros, significado, acceso y uso explicados; ejemplo ejecutado. |
| Distinguir listas de Python y arreglos tipados | CUMPLE | 9.1 y 9.3: listas dinámicas con tipos diferentes; representación introductoria, sin confundir bibliotecas. |
| Definir índice y subíndice y explicar su utilidad | CUMPLE | 9.2, p. 4: posición y acceso con corchetes. |
| Explicar inicio en cero y relación longitud/último índice | CUMPLE | 9.2: convención; longitud 4, último índice 3; generalización longitud menos uno. |
| Consultar nombres[0] y nombres[2] | CUMPLE | 9.2: Ana y Carlos; ejemplo con María; ejecución del ejemplo comprobada. |
| Modificar nombres[1] y mostrar resultado | CUMPLE | 9.2: Luis es reemplazado por Pedro; lista [Ana, Pedro, Carlos, María]. |
| Explicar IndexError y validar posiciones inexistentes | CUMPLE | 9.2: nombres[4] no existe; main.py valida de 0 a 4 antes de consultar. |
| Definir vector y relación con arreglo | CUMPLE | 9.3, p. 4: arreglo unidimensional representado por una lista. |
| Explicar unidimensional | CUMPLE | 9.3: un solo índice; no es una tabla de filas y columnas. |
| Características: orden, índices, varios valores, recorrido, consulta y modificación | CUMPLE | 9.3 y aplicación práctica, pp. 4–7. |
| Ejemplo for con edades [18, 21, 19, 25, 20] | CUMPLE | 9.3: código y las cinco iteraciones explicados; salida real comprobada. |
| Ejemplo while con las cinco edades | CUMPLE | 9.3, pp. 4–5: inicio en 0, condición, acceso, incremento y fin en 5; salida comprobada. |

## Parte II — Ejercicio práctico

| Requisito | Estado | Comprobación |
| --- | --- | --- |
| Vector con cinco elementos | CUMPLE | main.py: estudiantes y calificaciones contienen exactamente cinco elementos. |
| Acceso por índice | CUMPLE | Consulta, listado, modificación y búsqueda de main.py. |
| Modificación de un elemento | CUMPLE | Asignación calificaciones[indice] = nueva; registros 04 y 10. |
| Ciclo para recorrer el vector | CUMPLE | for en mostrar_calificaciones, calcular_promedio, mostrar_estado y buscar_estudiante. |
| Condición if | CUMPLE | Validación, búsqueda, clasificación y menú; también elif y else. |
| Operación de cálculo o búsqueda | CUMPLE | Promedio, extremos y búsqueda; registros 02, 07, 08 y 10. |
| Resultados al usuario | CUMPLE | print en menú y funciones; once transcripciones de ejecuciones reales. |
| Mostrar estudiantes y calificaciones | CUMPLE | Opción 1; registro 01 y 04. |
| Consultar por índice | CUMPLE | Opción 2; Carlos 92 con índice 2; registro 03. |
| Calcular promedio general | CUMPLE | Opción 3; registro 02: 75.20. |
| Mostrar máximo y mínimo | CUMPLE | Opciones 4 y 5 presentes; cálculos del resumen ejecutados: 92 y 58, registro 08. |
| Identificar y contar aprobados y reprobados | CUMPLE | Opciones 6 y 7; registro 05: 3 y 2. |
| Modificar una calificación | CUMPLE | Opción 8; Luis 67 a 80, registros 04 y 10. |
| Buscar estudiantes | CUMPLE | Opción 9; búsqueda lUiS con espacios y Sofia no registrado, registro 07. |
| Mostrar resumen general | CUMPLE | Opción 10; registros 08, 09 y 10. |
| Salir del programa | CUMPLE | Opción 0; cierre correcto en las once sesiones, incluida la directa 11. |
| Validar letras, índices, opciones y notas fuera de rango | CUMPLE | Registro 06: letras, opción 99, índices 9/-1, notas -5/101/abc; corrección y continuidad. |
| Total, promedio, máximo, mínimo y grupos iniciales | CUMPLE | 376; 75.20; 92; 58; 3 aprobados y 2 reprobados. Comprobación matemática y registros reales. |
| 70 como regla del ejercicio, no norma oficial ITLA | CUMPLE | MINIMO_APROBACION y comentario de main.py; investigación y README lo aclaran. |
| Actualizar vector, listado y cálculos tras Luis 67 a 80 | CUMPLE | Registros 04 y 10: lista [85,80,92,74,58], total 389, promedio 77.80, máximo 92, mínimo 58, grupos 4/1. |
| Conservar funcionamiento y nivel introductorio | CUMPLE | SHA256 de main.py sin cambios; no nuevas funcionalidades ni dependencias del programa. |

## Parte III — Repositorio GitHub

| Requisito | Estado | Comprobación |
| --- | --- | --- |
| Repositorio público accesible | CUMPLE | Consulta anónima HTTP 200; API indica private=false; evidencia tmp/auditoria_mandato/github.json. |
| main.py completo publicado | CUMPLE | HTTP 200; huella Git remota 688e385f4a81b07ab8bc7dff0107df5190ff2c04, igual al archivo local. |
| README publicado con descripción e instrucciones | CUMPLE | README público accesible, HTTP 200; versión anterior disponible; README local actualizado. |
| README local: nombre, descripción, objetivo, lenguaje, funciones, ejecución y estudiante | CUMPLE | Secciones revisadas; instrucciones py main.py y alternativa python main.py; once sesiones y ruta de entrega actualizadas. |
| Título exacto REPOSITORIO DEL PROYECTO | CUMPLE | PDF p. 7 y continuación p. 8; título literal y nombre Sistema de Calificaciones en Python. |
| Enlace real y clicable en PDF | CUMPLE | Anotación URI comprobada; URL pública mrcarlos1990/sistema-calificaciones-python-capitulo-ix. |
| No publicar sin autorización | CUMPLE | No se ejecutaron acciones de publicación. La versión definitiva permanece local. |

## Parte IV — Evidencias de ejecución

| Requisito | Estado | Comprobación |
| --- | --- | --- |
| Siete archivos disponibles | CUMPLE | captura_01.png a captura_07.png presentes; huellas SHA256 verificadas. |
| Capturas auténticas del proyecto real | CUMPLE | Aportadas por el estudiante; revisadas contra main.py, sus valores y mensajes. No se crearon imágenes. |
| Figura 1: código fuente desarrollado en Python | CUMPLE | PDF p. 9: main.py, validación y recorrido en VS Code; título y explicación. |
| Figura 2: creación de los vectores | CUMPLE | PDF p. 10: nombres y notas originales; título y explicación. |
| Figura 3: ejecución inicial | CUMPLE | PDF p. 11: py main.py y menú; título y explicación. |
| Figura 4: resultados generales | CUMPLE | PDF p. 12: listado, 75.20, 92, 58 y grupos 3/2; explicación coincide. |
| Figura 5: modificación | CUMPLE | PDF p. 13: mensaje Luis antes 67, ahora 80; no se afirma que la imagen muestre un listado posterior. |
| Figura 6: índices incorrectos | CUMPLE | PDF p. 14: índice 9 rechazado y consulta corregida a 2; explicación coincide. |
| Figura 7: finalización correcta | CUMPLE | PDF p. 15: opción 0, mensaje de cierre y retorno a terminal. |
| Número, título y explicación de cada figura | CUMPLE | Siete títulos actualizados al mandato; figuras.json y PDF. |
| Imágenes completas, legibles, proporcionales y del proyecto | CUMPLE | Siete páginas horizontales; revisión visual; dimensiones y píxeles incrustados iguales a los originales. |

## Parte V — Explicación del código

| Requisito | Estado | Comprobación |
| --- | --- | --- |
| Al menos tres fragmentos reales | CUMPLE | Ocho fragmentos, pp. 6–7; cotejo automático con main.py conservando sangría contextual. |
| Creación de vectores explicada | CUMPLE | Fragmento 1: cinco nombres/notas y correspondencia por índice. |
| Recorrido por índices explicado | CUMPLE | Fragmento 3: len=5 y range(5), índices 0–4. |
| Promedio explicado | CUMPLE | Fragmento 5: acumulador, total 376, división por 5 y formato 75.20. |
| Modificación explicada | CUMPLE | Fragmento 6: anterior, asignación y mensaje; nuevo promedio 77.80. |
| Validación de índices explicada | CUMPLE | Fragmento 8: función leer_entero real; ValueError, límites y while. |
| Condiciones de aprobados/reprobados explicadas | CUMPLE | Fragmento 4: comparación con MINIMO_APROBACION y contador. |
| Acceso y búsqueda adicionales correctos | CUMPLE | Fragmentos 2 y 7; índice 2 y búsqueda sin distinguir mayúsculas, sin eliminar tildes. |
| Resultados esperados y relación con conceptos | CUMPLE | Cada explicación relaciona el fragmento con listas, índices, ciclos, condiciones o cálculos. |

## Parte VI — Casos de prueba

| Requisito | Estado | Comprobación |
| --- | --- | --- |
| Mínimo de tres pruebas distintas | CUMPLE | Once sesiones ejecutadas correctamente; un método unittest con subTest por sesión. |
| Tabla con número, datos, esperado, obtenido y estado | CUMPLE | PDF pp. 16–17; resultados leídos de resultados.json, sin copiar resultados ficticios. |
| Promedio original 75.20 | CUMPLE | Sesión 02; ejecución_02.txt. |
| Modificar Luis 67 a 80 y consultar nuevo valor | CUMPLE | Sesión 04; listado actualizado y promedio 77.80; sesión 10 verifica resumen. |
| Contar tres aprobados originales | CUMPLE | Sesión 05; Ana, Carlos y Maria; también dos reprobados. |
| Índice inválido 9 y mensaje fuera de rango | CUMPLE | Sesión 06; transcripción conserva entrada 9 y rechazo entre 0 y 4. |
| Índice válido 2 devuelve Carlos 92 | CUMPLE | Sesión 03 y corrección dentro de sesión 06. |
| Finalizar con opción 0 | CUMPLE | Sesión 11 dedicada y cierre normal en todas las demás. |
| Pruebas adicionales sustentadas | CUMPLE | Búsqueda, extremos, límites 0/100/70 y resumen actualizado; registros 07–10. |
| No declarar APROBADA sin ejecutar | CUMPLE | Código de salida 0, STDERR vacío, salidas esperadas y cierre correcto en once procesos. |

## Parte VII — Conclusión

| Requisito | Estado | Comprobación |
| --- | --- | --- |
| Qué aprendí sobre arreglos | CUMPLE | Conclusión p. 17: agrupar datos y listas como vectores. |
| Importancia de índices | CUMPLE | Conclusión p. 17: localizar elementos y relacionar estudiante con nota. |
| Ventajas de vectores | CUMPLE | Conclusión p. 17: organizar y recorrer sin variables separadas. |
| Relación ciclos/arreglos | CUMPLE | Conclusión p. 17: for visita y procesa; while mantiene menú y valida. |
| Dificultad realmente confirmada | CUMPLE | Respuesta del estudiante en este chat: índices desde cero e índices inexistentes; incorporada p. 17. |
| Solución realmente confirmada | CUMPLE | Revisar código, probar entradas y validar rango; confirmada por el estudiante e incorporada p. 17. |
| Aplicación real | CUMPLE | Conclusión p. 18: calificaciones, inventarios y ventas. |
| Primera persona y sin instrucciones editoriales | CUMPLE | Siete preguntas respondidas expresamente; eliminados avisos de confirmación y revisión personal del PDF. |

## Parte VIII — Fuentes consultadas

| Requisito | Estado | Comprobación |
| --- | --- | --- |
| Organización y título en cada referencia | CUMPLE | Python Software Foundation; tres títulos oficiales, PDF p. 18. |
| Enlaces correctos y consultados | CUMPLE | Se abrieron introducción, estructuras de datos y control de flujo en docs.python.org/es/3/tutorial/. |
| Relación con investigación | CUMPLE | Listas y acceso; operaciones de listas; for y condiciones, según referencia. |
| Fecha real y formato uniforme | CUMPLE | Consulta 10 de octubre de 2026; organización, título, recurso, URL, fecha y uso. |
| Sin autores, libros o fuentes inventados | CUMPLE | Solo documentación oficial verificada; sin citas extensas copiadas. |

## Formato y control de calidad

| Requisito | Estado | Comprobación |
| --- | --- | --- |
| Documento único de entrega con nombre exacto | CUMPLE | ENTREGA_FINAL contiene solamente Amauri_Feliz_Actividad_Arreglos.pdf. |
| Conservar original sin sobrescribir | CUMPLE | documentacion/Amauri_Feliz_Actividad_Arreglos.pdf permanece como original; generación escribe en ENTREGA_FINAL. |
| Estructura obligatoria completa y en orden | CUMPLE | Portada; índice adicional; introducción; 9.1, 9.2, 9.3; desarrollo; código; repositorio; evidencias; pruebas; conclusión; fuentes. |
| Abrir y revisar todas las páginas | CUMPLE | 18 páginas renderizadas con Poppler; inspección visual de las páginas y revisión detallada de código, capturas y tabla. |
| Sin páginas vacías | CUMPLE | Cada página tiene contenido académico o evidencia; eliminado salto que dejaba una página casi vacía. |
| Tabla completa y sin cortes de filas | CUMPLE | Tabla de once casos en pp. 16–17; encabezado repetido; entradas separadas por punto y coma. |
| Texto y títulos dentro de márgenes | CUMPLE | Revisión visual, formato carta, márgenes de 54 puntos en cuerpo y páginas de evidencia. |
| Código monoespaciado y legible | CUMPLE | Courier, ocho fragmentos y ejemplos; sin líneas fuera del margen. |
| Ortografía, acentos y coherencia revisados | CUMPLE | Texto leído y revisado; María en ejemplo conceptual, Maria conservado en datos reales; títulos coherentes. |
| Sin instrucciones internas de inteligencia artificial | CUMPLE | Búsqueda de avisos editoriales y marcadores sin incidencias en PDF; conclusión limpia. |
| PDF válido y enlaces activos | CUMPLE | PdfReader abre 18 páginas; URI GitHub presente; repositorio HTTP 200. |
| Numeración e índice correctos | CUMPLE | Páginas 2–18 numeradas; índice actualizado por multiBuild y cotejado con secciones. |
| No modificar otros proyectos ni publicar cambios | CUMPLE | Todas las escrituras se realizaron en esta carpeta; main.py intacto; sin acciones de publicación. |

## Resultados y alcance

- 105 comprobaciones individuales: CUMPLE. Ninguna marcada NO CUMPLE o REQUIERE REVISIÓN después de las correcciones.
- Once sesiones reales del programa y cuatro ejemplos educativos comprobados; no son once métodos unittest.
- Programa principal sin cambios. Total inicial 376; promedio 75.20; máximo 92; mínimo 58; grupos 3/2. Después de Luis a 80: total 389, promedio 77.80, grupos 4/1.
- Siete imágenes originales intactas. Sus archivos llevan extensión .png, aunque internamente están codificados como JPEG; el PDF incorpora los mismos píxeles, sin deformarlos ni recomprimirlos con pérdida.
- README local actualizado. Repositorio público accesible y código main.py idéntico al publicado; PDF, capturas, nuevas pruebas y documentación revisada permanecen locales.
- La dificultad personal y su solución provienen de la respuesta expresa del estudiante. La auditoría verifica coherencia y cobertura; no certifica su desempeño en una evaluación oral.

## Correcciones realizadas

- Ejemplos exactos de calificaciones, nombres con María y edades; explicaciones de cinco iteraciones y del ciclo while.
- Sección exacta REPOSITORIO DEL PROYECTO y nombre Sistema de Calificaciones en Python.
- Ocho fragmentos reales explicados, incluida validación de índices.
- Títulos de las siete figuras ajustados al mandato y explicaciones contrastadas con sus imágenes.
- Conclusión con las siete respuestas; dificultad y solución confirmadas; sin instrucciones editoriales.
- Tabla con resultados reales y dos sesiones adicionales; eliminación de una página casi vacía y mejora de separadores de entradas.
- Generación segura en ENTREGA_FINAL; portada institucional copiada sin cambios del PDF original.

## Evidencia técnica de la revisión

- `evidencias/ejecucion_01.txt` a `ejecucion_11.txt` y `evidencias/resultados.json`.
- `evidencias/figuras.json`: títulos, explicaciones y huellas de las siete capturas.
- `tmp/auditoria_mandato/`: registros técnicos, ejemplos ejecutados, comprobaciones, copia de fuentes previas y renderizados de revisión; excluido de publicación por .gitignore.
- SHA256 del PDF de entrega: `a3341e8b12547bf7171920d68a537577c0c8e8118482078ea508860c1e191c4a`.

## Actualización pública pendiente

**REQUIERE REVISIÓN (publicación, fuera de la entrega académica del PDF):** antes de actualizar GitHub, el estudiante debe autorizar la publicación de este PDF, las capturas y los archivos revisados. Después debe comprobarse la igualdad de los archivos locales y publicados. No se afirma que la versión remota actual sea esta entrega definitiva.
