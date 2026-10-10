"""Pruebas reproducibles con la biblioteca estándar; ejecutan main.py."""
import json
from pathlib import Path
import subprocess
import sys
import unittest

RAIZ = Path(__file__).resolve().parents[1]
CASOS = [
    ("Visualización inicial", "1\n0\n", ["0. Ana: 85", "1. Luis: 67", "2. Carlos: 92", "3. Maria: 74", "4. Pedro: 58"]),
    ("Promedio", "3\n0\n", ["Promedio general: 75.20"]),
    ("Consulta por índice", "2\n2\n0\n", ["Carlos: 92 puntos"]),
    ("Modificación", "8\n1\n80\n1\n3\n0\n", ["Luis: antes 67, ahora 80", "1. Luis: 80", "Promedio general: 77.80"]),
    ("Aprobados y reprobados", "6\n7\n0\n", ["Ana: 85", "Carlos: 92", "Maria: 74", "Cantidad: 3", "Luis: 67", "Pedro: 58", "Cantidad: 2"]),
    ("Validación y continuidad", "letras\n99\n2\n9\n-1\n2\n8\n0\n-5\n101\nabc\n90\n1\n0\n", ["escriba un número entero", "entre 0 y 10", "entre 0 y 4", "entre 0 y 100", "Ana: antes 85, ahora 90", "0. Ana: 90"]),
    ("Búsqueda", "9\n  lUiS  \n9\nSofia\n0\n", ["Índice 1. Luis: 67", "Estudiante no registrado."]),
    ("Extremos y resumen", "10\n0\n", ["Promedio general: 75.20", "Calificación más alta: 92", "Calificación más baja: 58", "Cantidad: 3", "Cantidad: 2"]),
    ("Límites y aprobación en 70", "8\n0\n0\n8\n1\n100\n8\n4\n70\n10\n0\n", ["Ana: antes 85, ahora 0", "Luis: antes 67, ahora 100", "Pedro: antes 58, ahora 70", "Promedio general: 67.20", "Cantidad: 4", "Cantidad: 1"]),
]


class PruebasCalificaciones(unittest.TestCase):
    def test_sesiones_reales(self):
        resultados = []
        carpeta = RAIZ / "evidencias"
        carpeta.mkdir(exist_ok=True)
        for numero, (nombre, entradas, esperados) in enumerate(CASOS, 1):
            with self.subTest(prueba=nombre):
                proceso = subprocess.run(
                    [sys.executable, str(RAIZ / "main.py")], input=entradas,
                    text=True, capture_output=True, encoding="utf-8",
                    env={**__import__("os").environ, "PYTHONIOENCODING": "utf-8"}, timeout=10)
                salida = proceso.stdout
                correcto = proceso.returncode == 0 and not proceso.stderr
                correcto = correcto and all(texto in salida for texto in esperados)
                correcto = correcto and "Programa finalizado correctamente." in salida
                (carpeta / f"ejecucion_{numero:02}.txt").write_text(
                    "CONTEXTO: ejecución del ejercicio con los datos de ejemplo fijados por el enunciado.\n"
                    "Las notas modificadas son entradas de demostración; no se consultan expedientes académicos.\n\n"
                    "ENTRADAS (una por línea):\n" + entradas + "\nSALIDA REAL:\n" + salida
                    + "\nSTDERR:\n" + proceso.stderr + f"\nCódigo de salida: {proceso.returncode}\n", encoding="utf-8")
                resultados.append({"prueba": nombre, "entradas": entradas.strip().replace("\n", " → "),
                    "esperado": "; ".join(esperados), "obtenido": "; ".join(t for t in esperados if t in salida),
                    "estado": "APROBADA" if correcto else "FALLIDA"})
                self.assertTrue(correcto, salida + proceso.stderr)
        (carpeta / "resultados.json").write_text(json.dumps(resultados, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    unittest.main(verbosity=2)
