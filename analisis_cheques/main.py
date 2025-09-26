import os
import shutil
import pandas as pd

import constants as const


def dividir_excel(archivo_entrada: str, separador: str) -> list[pd.DataFrame]:
    """
    Divide el archivo Excel en bloques de datos según un separador.
    """
    os.makedirs("docs", exist_ok=True)

    df: pd.DataFrame = pd.read_excel(
        archivo_entrada, sheet_name=const.NOMBRE_HOJA, header=None
    )
    df["grupo"] = (df[0] == separador).cumsum()
    datos_combinados: list[pd.DataFrame] = []

    for _, datos in df.groupby("grupo"):
        datos_filtrados: pd.DataFrame = datos[datos[0] != separador]

        if (
            not datos_filtrados.empty
            and str(datos_filtrados.iloc[0, 0]).strip() == "Código:"
        ):
            columnas_fecha: list[int] = [2, 3]
            for col in columnas_fecha:
                datos_filtrados.loc[:, col] = pd.to_datetime(
                    datos_filtrados[col], format="%m/%d/%Y", errors="coerce"
                ).dt.strftime("%d-%m-%Y")
            datos_combinados.append(datos_filtrados)

    return datos_combinados


def filtrar_y_modificar_datos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filtra filas innecesarias y ajusta los datos.
    """
    df_filtrado = df[~df[0].astype(str).str.contains("TOTAL", na=False)]
    df_filtrado = df_filtrado[
        df_filtrado[0].astype(str).str.contains(r"CH|DP", na=False)
    ]
    codigo: int = df.iloc[0, 1]  # type: ignore
    nombre: str = df.iloc[0, 4]  # type: ignore
    df_filtrado[0] = codigo
    df_filtrado[1] = nombre
    df_filtrado.drop(columns=[6, 7, 8, 9], inplace=True)
    df_filtrado[10] = (
        pd.to_numeric(df_filtrado[10], errors="coerce").fillna(0)
        + pd.to_numeric(df_filtrado[11], errors="coerce").fillna(0) * -1
    )
    df_filtrado.drop(columns=[11, 12], inplace=True)
    df_filtrado.reset_index(drop=True, inplace=True)
    df_filtrado: pd.DataFrame = df_filtrado.drop(index=0)

    return df_filtrado


def procesar_archivos(
    archivo_entrada: str, separador: str, archivo_salida: str
) -> None:
    """
    Procesa el archivo Excel: divide, filtra, modifica y genera un archivo final.
    """
    datos_combinados: list[pd.DataFrame] = dividir_excel(archivo_entrada, separador)

    if not datos_combinados:
        print("No se generaron datos. Finalizando proceso.")
        return

    datos_modificados: list[pd.DataFrame] = [
        filtrar_y_modificar_datos(df) for df in datos_combinados
    ]
    df_final: pd.DataFrame = pd.concat(datos_modificados, ignore_index=True)
    df_final.to_excel(archivo_salida, index=False, header=False)

    limpiar()
    print("¡Proceso completado! 🎉")


def limpiar() -> None:
    """
    Elimina la carpeta temporal 'docs' si existe.
    """
    if os.path.exists("docs"):
        shutil.rmtree("docs")


if __name__ == "__main__":
    procesar_archivos(const.ARCHIVO_ENTRADA, const.SEPARADOR, const.ARCHIVO_SALIDA)
