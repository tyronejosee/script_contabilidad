import pandas as pd

from constants import (
    ARCHIVO_ENTRADA,
    ARCHIVO_SALIDA,
    NOMBRE_HOJA,
    COLUMNA_DEBITO,
    COLUMNA_CREDITO,
    COLUMNAS_NECESARIAS,
)


def eliminar_ceros_ambos_lados(df: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina filas donde tanto el Débito como el Crédito son 0 o nulos.
    """
    df = df.copy()
    df[COLUMNA_DEBITO] = pd.to_numeric(df[COLUMNA_DEBITO], errors="coerce").fillna(0)
    df[COLUMNA_CREDITO] = pd.to_numeric(df[COLUMNA_CREDITO], errors="coerce").fillna(0)
    return df[~((df[COLUMNA_DEBITO] == 0) & (df[COLUMNA_CREDITO] == 0))]


def procesar_excel(archivo_entrada: str, archivo_salida: str) -> None:
    """
    Procesa el archivo Excel con la hoja 'id'.
    """
    try:
        df = pd.read_excel(
            archivo_entrada, sheet_name=NOMBRE_HOJA, header=0, skiprows=[1, 2]
        )
    except ValueError:
        raise ValueError("La hoja no existe en el archivo Excel.")

    if not all(col in df.columns for col in COLUMNAS_NECESARIAS):
        raise ValueError(f"Faltan columnas necesarias: {COLUMNAS_NECESARIAS}")

    df_filtrado = eliminar_ceros_ambos_lados(df)
    df_filtrado.to_excel(archivo_salida, index=False)
    print(f"Archivo guardado en: {archivo_salida}")


if __name__ == "__main__":
    procesar_excel(ARCHIVO_ENTRADA, ARCHIVO_SALIDA)
