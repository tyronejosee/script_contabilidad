from io import BytesIO
import os

from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
import pandas as pd

import constants as const


def crear_carpeta_salida(carpeta: str) -> None:
    """
    Crea la carpeta de salida si no existe.
    """
    os.makedirs(carpeta, exist_ok=True)


def cargar_datos_excel(archivo_excel: str) -> pd.DataFrame | None:
    """
    Carga los datos desde un archivo Excel.
    """
    try:
        df = pd.read_excel(archivo_excel)
        return df
    except Exception as e:
        print(f"Error al cargar el archivo Excel: {e}")
        return None


def agregar_texto_a_pdf(
    escritor: PdfWriter,
    datos: dict,
    plantilla_pdf: str,
    numero_pagina: int,
) -> None:
    """
    Agrega texto sobre una plantilla PDF en la página indicada.
    """
    paquete = BytesIO()
    c = canvas.Canvas(paquete, pagesize=const.TAMANO_PAGINA)
    dibujar_guias(c) if const.LINEAS_GUIA else None
    insertar_texto(c, datos, numero_pagina)
    c.save()
    paquete.seek(0)
    superposicion = PdfReader(paquete)
    pagina_superpuesta = superposicion.pages[0]
    lector = PdfReader(plantilla_pdf)
    pagina = lector.pages[numero_pagina]
    pagina.merge_page(pagina_superpuesta)
    escritor.add_page(pagina)


def dibujar_guias(c: canvas.Canvas) -> None:
    """
    Dibuja líneas de guía en la página para ayudar con la maquetación.
    """
    # Líneas rojas
    c.setStrokeColorRGB(1, 0, 0)
    c.setLineWidth(1.5)

    for y in range(0, 800, 100):
        c.line(0, y, 600, y)

    for x in range(0, 600, 100):
        c.line(x, 0, x, 800)

    # Líneas grises
    c.setStrokeColorRGB(0.7, 0.7, 0.7)
    c.setLineWidth(0.5)

    for y in range(0, 800, 10):
        c.line(0, y, 600, y)

    for x in range(0, 600, 10):
        c.line(x, 0, x, 800)


def insertar_texto(c: canvas.Canvas, datos: dict, numero_pagina: int) -> None:
    """
    Inserta texto en posiciones específicas de la página.
    """
    c.setFillColorRGB(0, 0, 0)
    c.setFont(const.TIPO_FUENTE, const.TAMANO_FUENTE)

    if numero_pagina == 0:
        c.drawString(150, 632, f"{datos['Ubicación']}")
        c.drawString(260, 632, f"{datos['Día']}")
        c.drawString(340, 632, f"{datos['Mes']}")
        c.drawString(130, 618, f"{datos['Empleador']}")

    elif numero_pagina == 1:
        c.drawString(110, 220, f"{datos['Nombre Completo']}")
        c.drawString(130, 632, f"{datos['Direccion']}")
        c.drawString(150, 730, f"{datos['Telefono']}")
        c.drawString(150, 710, f"{datos['Email']}")


def generar_pdfs(df: pd.DataFrame, carpeta_salida: str, plantilla_pdf: str) -> None:
    """
    Genera un PDF para cada fila del DataFrame usando una plantilla.
    """
    for _, fila in df.iterrows():
        datos_pagina_1 = {
            "Ubicación": "Santiago",
            "Día": "02",
            "Mes": "Enero",
            "Empleador": "Falseto Falasio Ronaldo Reyes",
            "Nombre": fila["Nombre"],
            "Apellido": fila["Apellido"],
            "Edad": fila["Edad"],
        }
        nombre_completo = fila["Nombre"] + " " + fila["Apellido"]
        datos_pagina_2 = {
            "Nombre Completo": nombre_completo,
            "Apellido": fila["Apellido"],
            "Direccion": "Prueba de Dirección",
            "Telefono": "Prueba de Telefono",
            "Email": "Prueba de Email",
        }
        datos_combinados = [datos_pagina_1, datos_pagina_2]
        salida_pdf: str = f"{carpeta_salida}/{fila['Nombre']} {fila['Apellido']}.pdf"
        escritor = PdfWriter()

        agregar_texto_a_pdf(
            escritor, datos_combinados[0], plantilla_pdf, numero_pagina=0
        )
        agregar_texto_a_pdf(
            escritor, datos_combinados[1], plantilla_pdf, numero_pagina=1
        )

        with open(salida_pdf, "wb") as archivo_pdf:
            escritor.write(archivo_pdf)

        print(f"PDF generado {salida_pdf} ✅")
    print("Todos los PDFs han sido generados. 🎉")


def main() -> None:
    """
    Función principal del programa.
    """
    crear_carpeta_salida(const.CARPETA_SALIDA)

    df = cargar_datos_excel(const.ARCHIVO_ENTRADA)
    if df is not None:
        generar_pdfs(df, const.CARPETA_SALIDA, const.PLANTILLA_PDF)


if __name__ == "__main__":
    main()
