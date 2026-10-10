"""Ejercicio de listas relacionadas: Capítulo IX, ITLA.

Los cinco nombres y notas son los datos de ejemplo fijados por el enunciado.
Las modificaciones de las pruebas también son entradas de demostración.
"""

MINIMO_APROBACION = 70  # Regla de este ejercicio, no una política del ITLA.


def leer_entero(mensaje, minimo, maximo):
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("Entrada incorrecta: escriba un número entero.")
            continue
        if minimo <= valor <= maximo:
            return valor
        print(f"Valor fuera de rango: debe estar entre {minimo} y {maximo}.")


def mostrar_calificaciones(estudiantes, calificaciones):
    for indice in range(len(estudiantes)):
        print(f"{indice}. {estudiantes[indice]}: {calificaciones[indice]} puntos")


def calcular_promedio(calificaciones):
    total = 0
    for nota in calificaciones:
        total = total + nota
    return total / len(calificaciones)


def mostrar_estado(estudiantes, calificaciones, aprobados):
    cantidad = 0
    for indice in range(len(estudiantes)):
        aprobo = calificaciones[indice] >= MINIMO_APROBACION
        if aprobo == aprobados:
            print(f"{estudiantes[indice]}: {calificaciones[indice]} puntos")
            cantidad = cantidad + 1
    print(f"Cantidad: {cantidad}")


def buscar_estudiante(estudiantes, nombre):
    for indice in range(len(estudiantes)):
        if estudiantes[indice].lower() == nombre.strip().lower():
            return indice
    return -1


def main():
    # El mismo índice relaciona cada nombre con su calificación.
    estudiantes = ["Ana", "Luis", "Carlos", "Maria", "Pedro"]
    calificaciones = [85, 67, 92, 74, 58]
    while True:
        print("\n========================================")
        print("       SISTEMA DE CALIFICACIONES")
        print("========================================")
        print("1. Mostrar estudiantes y calificaciones")
        print("2. Consultar calificación por índice")
        print("3. Calcular promedio general")
        print("4. Mostrar calificación más alta")
        print("5. Mostrar calificación más baja")
        print("6. Mostrar estudiantes aprobados")
        print("7. Mostrar estudiantes reprobados")
        print("8. Modificar una calificación")
        print("9. Buscar estudiante")
        print("10. Mostrar resumen general")
        print("0. Salir")
        opcion = leer_entero("Seleccione una opción: ", 0, 10)
        if opcion == 0:
            print("Programa finalizado correctamente.")
            break
        elif opcion == 1:
            mostrar_calificaciones(estudiantes, calificaciones)
        elif opcion == 2:
            indice = leer_entero("Índice del estudiante (0 a 4): ", 0, 4)
            print(f"{estudiantes[indice]}: {calificaciones[indice]} puntos")
        elif opcion == 3:
            print(f"Promedio general: {calcular_promedio(calificaciones):.2f}")
        elif opcion == 4:
            print(f"Calificación más alta: {max(calificaciones)}")
        elif opcion == 5:
            print(f"Calificación más baja: {min(calificaciones)}")
        elif opcion == 6:
            mostrar_estado(estudiantes, calificaciones, True)
        elif opcion == 7:
            mostrar_estado(estudiantes, calificaciones, False)
        elif opcion == 8:
            indice = leer_entero("Índice a modificar (0 a 4): ", 0, 4)
            nueva = leer_entero("Nueva calificación (0 a 100): ", 0, 100)
            anterior = calificaciones[indice]
            calificaciones[indice] = nueva
            print(f"{estudiantes[indice]}: antes {anterior}, ahora {nueva} puntos")
        elif opcion == 9:
            indice = buscar_estudiante(estudiantes, input("Nombre del estudiante: "))
            if indice == -1:
                print("Estudiante no registrado.")
            else:
                print(f"Índice {indice}. {estudiantes[indice]}: {calificaciones[indice]} puntos")
        else:
            mostrar_calificaciones(estudiantes, calificaciones)
            print(f"Promedio general: {calcular_promedio(calificaciones):.2f}")
            print(f"Calificación más alta: {max(calificaciones)}")
            print(f"Calificación más baja: {min(calificaciones)}")
            print("Aprobados:")
            mostrar_estado(estudiantes, calificaciones, True)
            print("Reprobados:")
            mostrar_estado(estudiantes, calificaciones, False)


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nPrograma finalizado: entrada interrumpida.")
