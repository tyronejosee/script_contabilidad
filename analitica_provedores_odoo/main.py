import pandas as pd

from constants import (
    ARCHIVO_ENTRADA,
    ARCHIVO_SALIDA,
    NOMBRE_HOJA,
    COLUMNA_EMPRESA,
    COLUMNA_DEBITO,
    COLUMNA_CREDITO,
    COLUMNAS_NECESARIAS,
)


def eliminar_pares_cruzados(grupo: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina pares donde un monto aparece una vez como Débito y otra como Crédito
    dentro del mismo grupo (misma empresa), ignorando ceros y nulos.
    """
    grupo = grupo.copy()
    grupo[COLUMNA_DEBITO] = pd.to_numeric(
        grupo[COLUMNA_DEBITO], errors="coerce"
    ).fillna(0)
    grupo[COLUMNA_CREDITO] = pd.to_numeric(
        grupo[COLUMNA_CREDITO], errors="coerce"
    ).fillna(0)
    grupo["__idx"] = grupo.index

    debitos = grupo[grupo[COLUMNA_DEBITO] != 0][COLUMNA_DEBITO].tolist()
    creditos = grupo[grupo[COLUMNA_CREDITO] != 0][COLUMNA_CREDITO].tolist()
    comunes = set(debitos).intersection(set(creditos))
    indices_a_eliminar = set()

    for monto in comunes:
        idx_debito = grupo[
            (grupo[COLUMNA_DEBITO] == monto) & (~grupo.index.isin(indices_a_eliminar))
        ].head(1)["__idx"]
        idx_credito = grupo[
            (grupo[COLUMNA_CREDITO] == monto) & (~grupo.index.isin(indices_a_eliminar))
        ].head(1)["__idx"]

        if not idx_debito.empty and not idx_credito.empty:
            indices_a_eliminar.update([idx_debito.values[0], idx_credito.values[0]])

    return grupo[~grupo["__idx"].isin(indices_a_eliminar)].drop(columns="__idx")


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

    df_filtrado = df.groupby(COLUMNA_EMPRESA, group_keys=False)[df.columns].apply(
        eliminar_pares_cruzados
    )
    df_filtrado = df_filtrado.sort_values(by=COLUMNA_EMPRESA, ascending=True)
    df_filtrado.to_excel(archivo_salida, index=False)
    print(f"Archivo guardado en: {archivo_salida}")


if __name__ == "__main__":
    procesar_excel(ARCHIVO_ENTRADA, ARCHIVO_SALIDA)
