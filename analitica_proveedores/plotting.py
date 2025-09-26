import pandas as pd
import matplotlib.pyplot as plt

import constants as const


def procesar_y_graficar_excel(input_file: str) -> None:
    """
    Procesa y grafica los datos de un Excel con la hoja 'Plotting'.
    """
    try:
        df: pd.DataFrame = pd.read_excel(
            input_file, sheet_name=const.NOMBRE_HOJA_PLOTTING
        )
    except ValueError as e:
        print(f"Error leyendo el archivo Excel: {e}")

    if not all(col in df.columns for col in const.COLUMNAS_NECESARIAS):
        print(f"Faltan columnas necesarias: {const.COLUMNAS_NECESARIAS}")
        return

    for col in [const.COLUMNA_ABONOS, const.COLUMNA_CARGOS]:
        df[col] = df[col].replace({",": ""}, regex=True)
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(
        subset=[const.COLUMNA_FICHA, const.COLUMNA_ABONOS, const.COLUMNA_CARGOS]
    )
    agrupado: pd.DataFrame = df.groupby(const.COLUMNA_FICHA).agg(
        {const.COLUMNA_ABONOS: "sum", const.COLUMNA_CARGOS: "sum"}
    )
    agrupado.index = agrupado.index.str.split().str[0:2].str.join(" ")
    fichas = agrupado.index
    abonos = agrupado[const.COLUMNA_ABONOS]
    cargos = agrupado[const.COLUMNA_CARGOS]

    plt.figure(figsize=(10, 4))
    plt.bar(fichas, abonos, label="Abonos", color="skyblue")
    plt.bar(fichas, cargos, label="Cargos", bottom=abonos, color="lightcoral")
    plt.xlabel("Ficha")
    plt.ylabel("Monto Total")
    plt.title("Totales de Abonos y Cargos por Ficha")
    plt.legend()
    plt.xticks(rotation=30, fontsize=4, ha="right")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    procesar_y_graficar_excel(const.ARCHIVO_PLOTTING)
