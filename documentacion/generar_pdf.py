"""Herramienta de documentación; no es parte del programa académico.

Requiere reportlab y pypdf. El programa principal no requiere esos paquetes.
"""
import json
import hashlib
from io import BytesIO
from pathlib import Path
import re
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, PageBreak,
    Preformatted, LongTable, TableStyle, KeepTogether, Image, NextPageTemplate,
)
from reportlab.platypus.tableofcontents import TableOfContents
from pypdf import PdfReader, PdfWriter
from PIL import Image as ImagenOriginal

RAIZ = Path(__file__).resolve().parents[1]
ORIGINAL = RAIZ / "documentacion" / "Amauri_Feliz_Actividad_Arreglos.pdf"
SALIDA = RAIZ / "ENTREGA_FINAL" / "Amauri_Feliz_Actividad_Arreglos.pdf"
estilos = getSampleStyleSheet()
estilos.add(ParagraphStyle(name="TextoAcademico", fontName="Helvetica", fontSize=10.5,
    leading=15, alignment=TA_JUSTIFY, spaceAfter=9, allowWidows=0, allowOrphans=0))
estilos.add(ParagraphStyle(name="TituloAcademico", fontName="Helvetica-Bold", fontSize=17,
    leading=22, textColor=colors.HexColor("#163852"), spaceAfter=14, spaceBefore=18, keepWithNext=True))
estilos.add(ParagraphStyle(name="SubtituloAcademico", fontName="Helvetica-Bold", fontSize=12,
    leading=16, textColor=colors.HexColor("#163852"), spaceBefore=10, spaceAfter=8, keepWithNext=True))
estilos.add(ParagraphStyle(name="CodigoAcademico", fontName="Courier", fontSize=8,
    leading=11, backColor=colors.HexColor("#F0F3F6"), borderPadding=8, spaceAfter=12))
estilos.add(ParagraphStyle(name="Celda", fontName="Helvetica", fontSize=8, leading=11))
estilos.add(ParagraphStyle(name="Portada", fontName="Helvetica-Bold", fontSize=24,
    leading=31, alignment=TA_CENTER, textColor=colors.HexColor("#163852"), spaceAfter=24))
estilos.add(ParagraphStyle(name="Centro", fontName="Helvetica", fontSize=12,
    leading=19, alignment=TA_CENTER, spaceAfter=12))


def pie(canvas, documento):
    canvas.saveState()
    if documento.page > 1:
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.HexColor("#536578"))
        ancho, alto = canvas._pagesize
        canvas.drawString(54, alto - 37, "ITLA | Introducción a la Programación | Capítulo IX")
        canvas.drawString(54, 33, "Amauri Feliz Valenzuela | 10 de octubre de 2026")
        canvas.drawRightString(ancho - 54, 33, str(documento.page))
    canvas.restoreState()


class Documento(BaseDocTemplate):
    def afterFlowable(self, elemento):
        if isinstance(elemento, Paragraph) and elemento.style.name == "TituloAcademico":
            titulo = elemento.getPlainText()
            if titulo != "Índice":
                clave = "seccion-" + str(self.seq.nextf("seccion"))
                self.canv.bookmarkPage(clave)
                self.notify("TOCEntry", (0, titulo, self.page, clave))


def parrafo(texto, estilo="TextoAcademico"):
    seguro = escape(texto)
    seguro = re.sub(r"https://[^\s<>]+", lambda m: '<link href="' + m[0].rstrip('.')
                   + '" color="#163852">' + m[0].rstrip('.') + '</link>'
                   + ('.' if m[0].endswith('.') else ''), seguro)
    return Paragraph(seguro, estilos[estilo])


def figuras_revisadas():
    figuras = json.loads((RAIZ / "evidencias/figuras.json").read_text(encoding="utf-8"))
    revisadas = []
    for figura in figuras:
        ruta = RAIZ / "evidencias" / figura["archivo"]
        if not figura["revisada"]:
            continue
        assert ruta.is_file(), f"Figura revisada ausente: {ruta.name}"
        assert hashlib.sha256(ruta.read_bytes()).hexdigest() == figura["sha256"], "Imagen modificada después de revisión"
        revisadas.append(figura)
    return revisadas


def agregar_figuras(contenido):
    figuras = figuras_revisadas()
    contenido.append(NextPageTemplate("figuras"))
    for figura in figuras:
        contenido.append(PageBreak())
        contenido.append(parrafo(figura["titulo"], "SubtituloAcademico"))
        # Incrusto los píxeles sin recompresión con pérdida; conservo el archivo original.
        datos = BytesIO()
        with ImagenOriginal.open(RAIZ / "evidencias" / figura["archivo"]) as original:
            original.convert("RGB").save(datos, format="PNG")
        datos.seek(0)
        imagen = Image(datos)
        escala = min(684 / imagen.imageWidth, 400 / imagen.imageHeight)
        imagen.drawWidth = imagen.imageWidth * escala
        imagen.drawHeight = imagen.imageHeight * escala
        contenido.append(imagen)
        contenido.append(Spacer(1, 12))
        contenido.append(parrafo(figura["explicacion"]))
    if len(figuras) < 7:
        contenido.append(parrafo(f"Capturas revisadas e incorporadas: {len(figuras)} de 7. "
                                 "El documento permanece pendiente de completar las figuras auténticas."))
    contenido.append(NextPageTemplate("academico"))
    contenido.append(PageBreak())


def tabla_pruebas():
    resultados = json.loads((RAIZ / "evidencias/resultados.json").read_text(encoding="utf-8"))
    filas = [[parrafo(t, "Celda") for t in ["Prueba", "Datos utilizados", "Resultado esperado", "Resultado obtenido", "Estado"]]]
    for i, resultado in enumerate(resultados):
        filas.append([parrafo(t, "Celda") for t in [f"{i+1}. {resultado['prueba']}", resultado["entradas"].replace(" → ", "; "),
            resultado["esperado"], resultado["obtenido"] + f". Registro {i+1:02}.", resultado["estado"]]])
    tabla = LongTable(filas, colWidths=[80, 100, 130, 130, 64], repeatRows=1, hAlign="LEFT")
    tabla.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#DCE8F1")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#BAC7D2")),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return tabla


def generar():
    assert ORIGINAL.is_file(), "El PDF original debe estar disponible"
    SALIDA.parent.mkdir(exist_ok=True)
    documento = Documento(str(SALIDA), pagesize=letter, leftMargin=54, rightMargin=54,
        topMargin=54, bottomMargin=54, title="Capítulo IX - Arreglos y Vectores",
        author="Amauri Feliz Valenzuela")
    documento.addPageTemplates(PageTemplate(id="academico",
        frames=Frame(54, 54, 504, 684, leftPadding=0, rightPadding=0,
                     topPadding=0, bottomPadding=0), onPage=pie))
    documento.addPageTemplates(PageTemplate(id="figuras", pagesize=landscape(letter),
        frames=Frame(54, 54, 684, 504, leftPadding=0, rightPadding=0,
                     topPadding=0, bottomPadding=0), onPage=pie))
    # Reservar una página; al finalizar se sustituye por la portada institucional exacta.
    contenido = [Spacer(1, 10), PageBreak(), parrafo("Índice", "TituloAcademico")]
    indice = TableOfContents()
    indice.levelStyles = [ParagraphStyle(name="EntradaIndice", fontName="Helvetica", fontSize=11,
        leading=17, spaceBefore=7)]
    contenido.extend([indice, PageBreak()])
    texto = (RAIZ / "documentacion/investigacion.md").read_text(encoding="utf-8")
    bloques = texto.split("\n\n")
    for bloque in bloques:
        bloque = bloque.strip()
        if not bloque:
            continue
        if bloque.startswith("# "):
            contenido.append(parrafo(bloque[2:], "TituloAcademico"))
        elif bloque.startswith("## "):
            contenido.append(parrafo(bloque[3:], "SubtituloAcademico"))
        elif bloque.startswith("```python"):
            codigo = bloque.removeprefix("```python\n").removesuffix("\n```")
            grupo = []
            if isinstance(contenido[-1], Paragraph) and contenido[-1].style.name == "SubtituloAcademico":
                grupo.append(contenido.pop())
            grupo.append(Preformatted(codigo, estilos["CodigoAcademico"]))
            contenido.append(KeepTogether(grupo))
        elif bloque == "{{TABLA_PRUEBAS}}":
            contenido.append(tabla_pruebas())
        elif bloque == "{{FIGURAS_REALES}}":
            agregar_figuras(contenido)
        else:
            contenido.append(parrafo(bloque.replace("\n", " ").replace("`", "")))
    documento.multiBuild(contenido)
    generado = PdfReader(str(SALIDA))
    original = PdfReader(str(ORIGINAL))
    escritor = PdfWriter()
    escritor.clone_document_from_reader(generado)
    portada = escritor.add_page(original.pages[0])
    primera = escritor.pages[0]
    for clave in list(primera.keys()):
        if clave not in ["/Parent", "/Type"]:
            del primera[clave]
    for clave, valor in portada.items():
        if clave not in ["/Parent", "/Type"]:
            primera[clave] = valor
    escritor.remove_page(len(escritor.pages) - 1)
    with SALIDA.open("wb") as archivo:
        escritor.write(archivo)
    lector = PdfReader(str(SALIDA))
    assert lector.pages[0].get_contents().get_data() == original.pages[0].get_contents().get_data()

    print(f"PDF generado: {len(lector.pages)} páginas, tamaño carta")
    assert all(sorted([float(p.mediabox.width), float(p.mediabox.height)]) == [612, 792] for p in lector.pages)
    extraido = "\n".join(p.extract_text() for p in lector.pages)
    for titulo in ["Introducción", "Objetivos", "9.1 ¿Qué es un arreglo?", "9.2 Índices y subíndices",
                   "9.3 Vectores y características", "Desarrollo del proyecto", "Herramientas y funcionamiento",
                   "Explicación del código", "REPOSITORIO DEL PROYECTO", "Evidencias de ejecución",
                   "Casos de prueba", "Conclusión", "Fuentes consultadas"]:
        assert titulo in extraido, titulo
    assert "{{TABLA_PRUEBAS}}" not in extraido
    assert "{{FIGURAS_REALES}}" not in extraido
    for figura in figuras_revisadas():
        assert figura["titulo"] in extraido
    print("Secciones, tabla y formato de página verificados.")


if __name__ == "__main__":
    generar()
