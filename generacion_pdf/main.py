import os
from io import BytesIO

import pandas as pd
from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# "Helvetica"
# "Helvetica-Bold"
# "Helvetica-Oblique"
# "Helvetica-BoldOblique"
# "Times-Roman"
# "Times-Bold"
# "Times-Italic"
# "Times-BoldItalic"
# "Courier"
# "Courier-Bold"
# "Courier-Oblique"
# "Courier-BoldOblique"
# "Symbol"
# "ZapfDingbats"


INPUT_FILE = "input.xlsx"
TEMPLATE_PDF = "template.pdf"
OUTPUT_DIR = "output"
LINES = False
FONT_TYPE = "Helvetica"
FONT_SIZE = 11
PAGE_SIZE = letter
GUIDE_INTERVAL = 50


def create_output_dir(output_dir) -> None:
    os.makedirs(output_dir, exist_ok=True)


def load_excel_data(excel_file) -> pd.DataFrame | None:
    try:
        df = pd.read_excel(excel_file)
        return df
    except Exception as e:
        print(f"Error al cargar el archivo Excel: {e}")
        return None


def add_text_to_pdf(
    writer,
    data,
    template_pdf,
    page_num,
    pages_to_edit=None,
) -> None:
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=PAGE_SIZE)
    draw_guides(c) if LINES else None
    insert_text(c, data, page_num)
    c.save()
    packet.seek(0)
    overlay = PdfReader(packet)
    overlay_page = overlay.pages[0]
    reader = PdfReader(template_pdf)
    page = reader.pages[page_num]
    page.merge_page(overlay_page)
    writer.add_page(page)


def draw_guides(c) -> None:
    # Líneas rojas
    c.setStrokeColorRGB(1, 0, 0)
    c.setLineWidth(1.5)

    # Líneas horizontales (Rojas)
    for y in range(0, 800, 100):
        c.line(0, y, 600, y)

    # Líneas verticales (Rojas)
    for x in range(0, 600, 100):
        c.line(x, 0, x, 800)

    # Líneas grises
    c.setStrokeColorRGB(0.7, 0.7, 0.7)
    c.setLineWidth(0.5)

    # Líneas horizontales (Grises)
    for y in range(0, 800, 10):
        c.line(0, y, 600, y)

    # Líneas verticales (Grises)
    for x in range(0, 600, 10):
        c.line(x, 0, x, 800)


def insert_text(c, data, page_num) -> None:
    c.setFillColorRGB(0, 0, 0)
    c.setFont(FONT_TYPE, FONT_SIZE)

    if page_num == 0:
        c.drawString(110, 630, f"{data['Nombre']}")
        c.drawString(150, 620, f"{data['Apellido']}")
        c.drawString(200, 610, f"{data['Edad']}")

    elif page_num == 1:
        c.drawString(110, 220, f"{data['Nombre Completo']}")
        c.drawString(130, 632, f"{data['Direccion']}")
        c.drawString(150, 730, f"{data['Telefono']}")
        c.drawString(150, 710, f"{data['Email']}")


def generate_pdfs(df, output_dir, template_pdf) -> None:
    for _, row in df.iterrows():
        # Datos para la primera página
        data_page_1 = {
            "Nombre": row["Nombre"],
            "Apellido": row["Apellido"],
            "Edad": row["Edad"],
        }

        # Datos para la segunda página
        full_name = row["Nombre"] + " " + row["Apellido"]

        data_page_2 = {
            "Nombre Completo": full_name,
            "Apellido": row["Apellido"],
            "Direccion": "Prueba de Dirección",
            "Telefono": "Prueba de Telefono",
            "Email": "Prueba de Email",
        }

        data_combined = [data_page_1, data_page_2]
        output_pdf: str = f"{output_dir}/{row['Nombre']} {row['Apellido']}.pdf"
        writer = PdfWriter()

        # Agregar páginas
        add_text_to_pdf(writer, data_combined[0], template_pdf, page_num=0)
        add_text_to_pdf(writer, data_combined[1], template_pdf, page_num=1)

        with open(output_pdf, "wb") as output_pdf_file:
            writer.write(output_pdf_file)

        print(f"PDF generado {output_pdf} ✅")

    print("Todos los PDFs han sido generados. 🎉")


def main() -> None:
    create_output_dir(OUTPUT_DIR)

    df = load_excel_data(INPUT_FILE)
    if df is not None:
        generate_pdfs(df, OUTPUT_DIR, TEMPLATE_PDF)


if __name__ == "__main__":
    main()
