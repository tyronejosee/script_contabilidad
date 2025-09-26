import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


def generar_datos_ejemplo() -> pd.DataFrame:
    """
    Crea un DataFrame de ejemplo con datos simulados.
    """
    data = {
        "Fecha": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05"],
        "Concepto": ["Ingreso", "Egreso", "Ingreso", "Egreso", "Ingreso"],
        "Monto": [100000, 50000, 200000, 30000, 150000],
    }
    return pd.DataFrame(data)


def generar_resumen(flujo_df) -> pd.DataFrame:
    """
    Genera un resumen agrupando por concepto.
    """
    return flujo_df.groupby("Concepto")["Monto"].sum()


def guardar_resumen_excel(resumen: pd.DataFrame, nombre_archivo: str) -> None:
    """
    Guarda el resumen en un archivo Excel.
    """
    resumen.to_excel(nombre_archivo)


def crear_grafico(resumen: pd.DataFrame, nombre_archivo: str) -> None:
    """
    Crea y guarda un gráfico de barras del resumen.
    """
    colores = [
        "green" if concepto == "Ingreso" else "red" for concepto in resumen.index
    ]

    resumen.plot(
        kind="bar",
        title="Resumen de Ingresos y Egresos",
        color=colores,
    )

    plt.xlabel("Concepto")
    plt.ylabel("Monto (CLP)")
    plt.tight_layout()
    plt.savefig(nombre_archivo)
    plt.close()


def guardar_reporte_pdf(resumen: pd.DataFrame, nombre_archivo: str) -> None:
    """
    Guarda el resumen y el gráfico en un archivo PDF.
    """

    with PdfPages(nombre_archivo) as pdf:
        plt.figure()
        colores = [
            "green" if concepto == "Ingreso" else "red" for concepto in resumen.index
        ]
        resumen.plot(kind="bar", title="Resumen de Ingresos y Egresos", color=colores)

        plt.xlabel("Concepto")
        plt.ylabel("Monto (CLP)")
        plt.tight_layout()
        pdf.savefig()
        plt.close()


def main() -> None:
    """
    Función principal para generar el reporte.
    """
    flujo_df = generar_datos_ejemplo()
    resumen = generar_resumen(flujo_df)

    guardar_resumen_excel(resumen, "output.xlsx")
    crear_grafico(resumen, "grafico_ingresos_egresos.png")
    guardar_reporte_pdf(resumen, "reporte_completo.pdf")
    print("Reporte generado y guardado exitosamente.")


if __name__ == "__main__":
    main()
