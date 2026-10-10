"""Comprueba el repositorio público sin credenciales ni sesión de GitHub."""
import hashlib
import json
from pathlib import Path
import subprocess
import urllib.request

RAIZ = Path(__file__).resolve().parents[1]
REPOSITORIO = "mrcarlos1990/sistema-calificaciones-python-capitulo-ix"


def obtener(url):
    solicitud = urllib.request.Request(url, headers={"User-Agent": "ITLA-verificacion-publica"})
    with urllib.request.urlopen(solicitud, timeout=30) as respuesta:
        assert respuesta.status == 200
        return respuesta.read()


def verificar():
    base = "https://api.github.com/repos/" + REPOSITORIO
    metadata = json.loads(obtener(base))
    assert metadata["private"] is False
    arbol = json.loads(obtener(base + "/git/trees/main?recursive=1"))
    assert not arbol.get("truncated")
    remoto = {entrada["path"]: entrada["sha"] for entrada in arbol["tree"] if entrada["type"] == "blob"}
    rutas = subprocess.check_output(["git", "ls-files", "-z"], cwd=RAIZ).decode().split("\0")
    comparados = []
    for relativo in filter(None, rutas):
        # La herramienta de comprobación puede prepararse antes de publicarse.
        contenido = (RAIZ / relativo).read_bytes()
        sha = hashlib.sha1(f"blob {len(contenido)}\0".encode() + contenido).hexdigest()
        assert remoto.get(relativo) == sha, f"Archivo diferente o ausente: {relativo}"
        comparados.append(relativo)
    pagina = obtener("https://github.com/" + REPOSITORIO)
    assert b"sistema-calificaciones-python-capitulo-ix" in pagina
    pdf = "ENTREGA_FINAL/Amauri_Feliz_Actividad_Arreglos.pdf"
    descargado = obtener("https://raw.githubusercontent.com/" + REPOSITORIO + "/main/" + pdf)
    assert descargado == (RAIZ / pdf).read_bytes()
    from io import BytesIO
    from pypdf import PdfReader
    assert len(PdfReader(BytesIO(descargado)).pages) == 17
    resultado = {"url": metadata["html_url"], "publico": True,
                 "acceso_sin_credenciales": True, "archivos_identicos": comparados,
                 "pdf_descargado_identico": True, "paginas_pdf": 17,
                 "pdf_sha256": hashlib.sha256(descargado).hexdigest(), "rama": "main", "tree_sha": arbol["sha"]}
    destino = RAIZ / "tmp/verificacion_publica.json"
    destino.parent.mkdir(exist_ok=True)
    destino.write_text(json.dumps(resultado, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Acceso público HTTP 200, {len(comparados)} archivos idénticos y PDF descargado idéntico.")


if __name__ == "__main__":
    verificar()
