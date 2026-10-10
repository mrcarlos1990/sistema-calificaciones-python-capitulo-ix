"""Audita solamente los archivos versionados de esta asignación.

No muestra el contenido de posibles credenciales. Requiere pypdf para leer el PDF.
"""
import hashlib
import json
from pathlib import Path
import re
import subprocess

from pypdf import PdfReader

RAIZ = Path(__file__).resolve().parents[1]
PATRONES = {
    "token de GitHub": r"(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})",
    "clave privada": r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
    "clave de AWS": r"(?:AKIA|ASIA)[A-Z0-9]{16}",
    "credencial asignada": r"(?im)^\s*(?:password|passwd|token|api_key|secret|contrase[nñ]a)\s*[:=]\s*[\"']?[^\s\"']{8,}",
    "correo privado": r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}",
    "ruta del equipo": r"(?i)C:[\\/](?:Users|PROYECTOS)",
}


def verificar():
    rutas = subprocess.check_output(["git", "ls-files", "-z"], cwd=RAIZ).decode("utf-8").split("\0")
    incidencias = []
    inventario = []
    for relativo in filter(None, rutas):
        ruta = RAIZ / relativo
        contenido = ruta.read_bytes()
        inventario.append({"archivo": relativo, "bytes": len(contenido),
                           "sha256": hashlib.sha256(contenido).hexdigest()})
        if ruta.suffix.lower() == ".pdf":
            texto = "\n".join(p.extract_text() for p in PdfReader(ruta).pages)
        elif ruta.suffix.lower() in (".png", ".jpg", ".jpeg"):
            continue  # Las imágenes requieren también inspección visual.
        else:
            texto = contenido.decode("utf-8")
        # Este archivo contiene patrones para detectar secretos, no credenciales.
        if ruta.name != "verificar_entrega.py":
            for nombre, patron in PATRONES.items():
                if re.search(patron, texto):
                    incidencias.append({"archivo": relativo, "motivo": nombre})
        if ruta.name in (".env", "local.properties", "release-signing.properties") or ruta.suffix in (".jks", ".keystore", ".pem", ".key"):
            incidencias.append({"archivo": relativo, "motivo": "archivo privado"})
        if any(parte in (".git", ".agents", ".codex", "tmp", "__pycache__") for parte in Path(relativo).parts):
            incidencias.append({"archivo": relativo, "motivo": "archivo ajeno a entrega"})
    informe = {"alcance": "Archivos versionados de la carpeta exclusiva de la asignación",
               "revision": "Detección de patrones y lectura del PDF; imágenes requieren revisión visual",
               "datos_academicos": "Nombre del estudiante, institución, profesor y usuario GitHub autorizados",
               "incidencias": incidencias, "inventario": inventario}
    destino = RAIZ / "tmp" / "revision_publicacion.json"
    destino.parent.mkdir(exist_ok=True)
    destino.write_text(json.dumps(informe, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Archivos revisados: {len(inventario)}. Incidencias: {len(incidencias)}.")
    for incidencia in incidencias:
        print(incidencia["archivo"], incidencia["motivo"])
    assert not incidencias, "Resolver incidencias antes de publicar."


if __name__ == "__main__":
    verificar()
