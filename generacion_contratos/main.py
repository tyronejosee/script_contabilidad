import os
import subprocess

import pandas as pd
from docx import Document
from docx.shared import Pt
from docx.oxml import ns

import constants as const


def replace_text(paragraph, replacements, font, font_size) -> None:
    for search, replacement in replacements.items():
        if search in paragraph.text:
            new_text = paragraph.text.replace(search, replacement)
            paragraph.clear()
            run = paragraph.add_run(new_text)
            run.font.size = Pt(font_size)
            run.font.name = font
            rFonts = run._element.rPr.rFonts
            rFonts.set(ns.qn("w:ascii"), font)
            rFonts.set(ns.qn("w:hAnsi"), font)
            rFonts.set(ns.qn("w:eastAsia"), font)
            rFonts.set(ns.qn("w:cs"), font)


def docx_to_pdf(docx_path, output_folder) -> None:
    libreoffice_path = r"C:\\Program Files\\LibreOffice\\program\\soffice.exe"

    if not os.path.exists(libreoffice_path):
        raise FileNotFoundError("No se encontró LibreOffice.")

    command = [
        libreoffice_path,
        "--headless",
        "--convert-to",
        "pdf",
        "--outdir",
        output_folder,
        docx_path,
    ]
    subprocess.run(command, check=True)


def convert_all_docx_to_pdf(output_folder) -> None:
    for file in os.listdir(output_folder):
        if file.endswith(".docx"):
            file_format: str = file.replace(".docx", "")
            docx_path: str = os.path.join(output_folder, file)
            try:
                docx_to_pdf(docx_path, output_folder)
                print(f"Documento convertido {file_format}.pdf ✅")
            except Exception as e:
                print(f"Error al convertir {file} a PDF: {e}")


def generate_documents(excel_path, template_path, output_folder) -> None:
    df: pd.DataFrame = pd.read_excel(excel_path)
    os.makedirs(output_folder, exist_ok=True)

    print("\nIniciando generación de Word...\n")
    for _, row in df.iterrows():
        doc = Document(template_path)
        replacements = {
            key: row.get(value, "") for key, value in const.PLACEHOLDERS.items()
        }

        for paragraph in doc.paragraphs:
            replace_text(
                paragraph,
                replacements,
                const.FONT_TYPE,
                const.FONT_SIZE,
            )

        file_name: str = f"{row[const.OUTPUT_FIELD]}.docx"
        docx_path: str = os.path.join(output_folder, file_name)

        doc.save(docx_path)
        print(f"Documento creado {file_name} ✅")

    print("\nIniciando conversión a PDF...\n")
    convert_all_docx_to_pdf(output_folder)


if __name__ == "__main__":
    generate_documents(
        const.INPUT_FILE,
        const.TEMPLATE_FILE,
        const.OUTPUT_FOLDER,
    )
