import re
import pandas as pd

import constants as const


def extraer_rut_y_nombre(ficha: str) -> tuple[str, str]:
    """
    Extrae RUT y nombre desde un string.
    Retorna (rut, nombre).
    """
    if not isinstance(ficha, str):
        return ("", "")

    match = re.search(r"(\d{1,2}\.?\d{3}\.?\d{3}-[\dkK])", ficha)
    if match:
        rut = match.group(1)
        nombre = ficha.replace(rut, "").strip(" -")
        return (rut, nombre)
    else:
        return ("", ficha.strip())


def procesar_excel(archivo_entrada: str, archivo_salida: str) -> None:
    """
    Procesa el archivo Excel con la hoja 'id'.
    """
    try:
        df = pd.read_excel(archivo_entrada, sheet_name=const.NOMBRE_HOJA)
    except ValueError:
        raise ValueError("La hoja no existe en el archivo Excel.")

    if not all(col in df.columns for col in const.COLUMNAS_NECESARIAS):
        raise ValueError(f"Faltan columnas necesarias: {const.COLUMNAS_NECESARIAS}")

    for col in [const.COLUMNA_ABONOS, const.COLUMNA_CARGOS, const.COLUMNA_SALDO]:
        df[col] = df[col].replace({",": ""}, regex=True)
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df[df[const.COLUMNA_FICHA] != const.VARIOS]
    df[const.COLUMNA_PIVOTE] = df[const.COLUMNA_SALDO].abs()
    df_grouped = df.groupby(
        [const.COLUMNA_FICHA, const.COLUMNA_NUMERO, const.COLUMNA_PIVOTE]
    )
    indices_a_eliminar = []

    for _, group in df_grouped:
        if len(group) == 2 and group[const.COLUMNA_SALDO].sum() == 0:
            indices_a_eliminar.extend(group.index)

    df_filtrado = df.drop(indices_a_eliminar)
    df_grouped = df_filtrado.groupby([const.COLUMNA_FICHA, const.COLUMNA_NUMERO])
    indices_a_eliminar_por_abonos_cargos = []

    for _, group in df_grouped:
        if (group[const.COLUMNA_ABONOS].sum() - group[const.COLUMNA_CARGOS].sum()) == 0:
            indices_a_eliminar_por_abonos_cargos.extend(group.index)

    df_filtrado: pd.DataFrame = df_filtrado.drop(indices_a_eliminar_por_abonos_cargos)
    df_filtrado["RUT"], df_filtrado["NOMBRE"] = zip(
        *df_filtrado[const.COLUMNA_FICHA].map(extraer_rut_y_nombre)
    )
    cols = df_filtrado.columns.tolist()
    idx = cols.index(const.COLUMNA_FICHA)
    cols = (
        cols[: idx + 1]
        + ["RUT", "NOMBRE"]
        + [
            col
            for col in cols
            if col not in ["RUT", "NOMBRE"] and col not in cols[: idx + 1]
        ]
    )
    df_filtrado = df_filtrado[cols]
    df_filtrado.to_excel(archivo_salida, index=False)
    print(f"Archivo guardado en: {archivo_salida}")


if __name__ == "__main__":
    procesar_excel(const.ARCHIVO_ENTRADA, const.ARCHIVO_SALIDA)
