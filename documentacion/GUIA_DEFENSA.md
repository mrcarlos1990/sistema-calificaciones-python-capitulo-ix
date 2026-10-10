# Guía breve para explicar el programa

- **¿Qué es un arreglo?** Es una estructura que reúne varios valores bajo un nombre y permite acceder a sus posiciones. En este ejercicio utilizo listas de Python.
- **¿Qué es un vector?** Un arreglo de una dimensión. Mis listas de nombres y notas tienen una sola secuencia de posiciones.
- **¿Qué es un índice?** Es el número que identifica una posición. El índice 2 relaciona a Carlos con su nota 92.
- **¿Por qué empieza en cero?** Python sigue esa convención: cero identifica el primer elemento, uno el segundo. No es una regla universal de todos los lenguajes. Cinco elementos ocupan los índices 0 a 4.
- **¿Cómo modifico una nota?** Valido el índice y la nueva nota y hago `calificaciones[indice] = nueva`. La lista de nombres no cambia.
- **¿Cómo calculo el promedio?** Acumulo las notas con `for` y divido el total entre `len(calificaciones)`. Inicialmente 376 / 5 = 75.20.
- **¿Cómo funciona `for`?** Repite una operación por cada nota o índice. En el listado uso el mismo índice para leer nombre y calificación.
- **¿Cómo funciona `while`?** Repite mientras su condición sea verdadera. `while True` mantiene el menú activo; `break` lo termina al elegir 0. También permite repetir una entrada inválida.
- **¿Para qué utilicé `if`?** Para seleccionar opciones, validar rangos y comparar cada nota con 70. `elif` evalúa otras opciones y `else` cubre el caso restante.
- **¿Qué aprendí?** Respuesta propuesta para revisar: aprendí a relacionar dos listas por sus índices, recorrerlas, cambiar valores y comprobar cálculos. Debo confirmar que puedo explicar estas operaciones y adaptar esta respuesta a mi aprendizaje real.

Practicar también: cambiar Luis a 80, comprobar promedio 77.80, explicar por qué habría cuatro aprobados y un reprobado, y mostrar que al reiniciar se recuperan las notas originales.
