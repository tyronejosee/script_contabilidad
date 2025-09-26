import os
import re

import pandas as pd

import constants as const


def limpiar_nombre(nombre: str) -> str:
    """
    Limpia el nombre de un archivo para que sea compatible con las reglas de ODOO.
    """
    return re.sub(r'[\\/*?:"<>|]', "", nombre).strip()


def normalizar_columna(col: str) -> str:
    """
    Normaliza las columnas para que sean compatibles con las reglas de ODOO.
    """
    col = col.strip()
    col = col.replace("�", "ó")
    col = col.replace("  ", " ")
    return col


def validar_estructura(df: pd.DataFrame) -> list[str]:
    """
    Valida la estructura del archivo Excel con la hoja 'Libro mayor'.
    """
    errores = []
    columnas_archivo = [normalizar_columna(c) for c in df.columns]

    for col in const.COLUMNAS_ESPERADAS:
        if col not in columnas_archivo:
            errores.append(f"Falta la columna obligatoria: '{col}'")

    if df.empty:
        errores.append("La hoja está vacía o no contiene datos.")
    return errores


def procesar_libro_mayor(input_file: str) -> None:
    """
    Procesa el archivo Excel con la hoja 'Libro mayor'.
    """
    if not os.path.exists(input_file):
        print(f"❌ Error: El archivo '{input_file}' no existe.")
        return

    try:
        xl = pd.ExcelFile(input_file)
    except Exception as e:
        print(f"❌ Error al leer el archivo Excel: {e}")
        return

    if const.COLUMNA_HOJA not in xl.sheet_names:
        print(f"❌ Error: La hoja '{const.COLUMNA_HOJA}' no existe en el archivo.")
        return

    df = xl.parse(const.COLUMNA_HOJA, dtype=str)
    df.columns = [normalizar_columna(c) for c in df.columns]
    df.fillna("", inplace=True)
    errores = validar_estructura(df)

    if errores:
        print("❌ Se encontraron errores en la estructura del archivo:\n")
        for err in errores:
            print(f"  - {err}")
        return

    cuentas: list = []
    cuenta_actual = None
    rows_actuales: list = []

    for _, row in df.iterrows():
        codigo = row["Código"].strip()
        nombre = row["Nombre de la cuenta"].strip()

        if codigo and nombre:
            if cuenta_actual and rows_actuales:
                cuentas.append((cuenta_actual, rows_actuales))
                rows_actuales = []
            cuenta_actual = (codigo, nombre)

        elif row["Código"].startswith("Total"):
            if cuenta_actual and rows_actuales:
                cuentas.append((cuenta_actual, rows_actuales))
                rows_actuales = []
            cuenta_actual = None

        elif cuenta_actual:
            nueva_fila = {
                "Código": cuenta_actual[0],
                "Nombre de la cuenta": cuenta_actual[1],
                "Comprobante": (
                    row["Código"].strip() or row["Nombre de la cuenta"].strip()
                ),
                "Fecha": row["Fecha"].strip(),
                "Comunicación": row["Comunicación"].strip(),
                "Empresa": row["Empresa"].strip(),
                "Moneda": row["Moneda"].strip(),
                "Debe": row["Debe"].strip(),
                "Haber": row["Haber"].strip(),
                "Saldo": "",
                "Balance": row["Balance"].strip(),
            }
            rows_actuales.append(nueva_fila)

    if cuenta_actual and rows_actuales:
        cuentas.append((cuenta_actual, rows_actuales))

    os.makedirs("output", exist_ok=True)

    for (codigo, nombre), filas in cuentas:
        df_out = pd.DataFrame(filas)
        df_out = df_out[~df_out["Comprobante"].str.startswith("Total ")]

        nombre_archivo = f"{codigo}_{limpiar_nombre(nombre)}.xlsx"
        ruta_archivo = os.path.join("output", nombre_archivo)
        print(f"🔄 Procesando archivo: '{nombre_archivo}'")
        df_out.to_excel(ruta_archivo, index=False)

    print(f"\n✅ {len(cuentas)} archivos generados en la carpeta `output/`.")


if __name__ == "__main__":
    procesar_libro_mayor("input.xlsx")
