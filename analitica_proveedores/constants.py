# Rutas de archivos
ARCHIVO_ENTRADA = "input.xlsx"
ARCHIVO_SALIDA = "output.xlsx"
ARCHIVO_PLOTTING = "output.xlsx"

# Nombre de la hoja
NOMBRE_HOJA = "id"
# NOMBRE_HOJA = "proveedores nacionales"
NOMBRE_HOJA_PLOTTING = "Sheet1"

# Columnas
COLUMNA_FICHA = "Ficha"
COLUMNA_FECHA = "Fecha"
COLUMNA_TIPO_DOC = "Tipo Doc."
COLUMNA_NUMERO = "Número"
COLUMNA_ABONOS = "Abonos $"
COLUMNA_CARGOS = "Cargos $"
COLUMNA_SALDO = "Saldo $"
COLUMNA_PIVOTE = "Saldo_Absoluto"
COLUMNAS_NECESARIAS = [
    COLUMNA_FICHA,
    COLUMNA_FECHA,
    COLUMNA_TIPO_DOC,
    COLUMNA_NUMERO,
    COLUMNA_ABONOS,
    COLUMNA_CARGOS,
    COLUMNA_SALDO,
]

# Valores que pueden aparecer en la columna 'Tipo Doc.'
VARIOS = "1-9 Varios"
