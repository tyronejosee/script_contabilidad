# Rutas de archivos
ARCHIVO_ENTRADA = "input.xlsx"
PLANTILLA_DOCX = "template.docx"
CAMPO_SALIDA = "NOMBRE_EMPRESA"
CARPETA_SALIDA = "output"

# Constantes
TIPO_FUENTE = "Calibri"
TAMANO_FUENTE = 11

# Clave: marcador en Word
# Valor: columna en Excel
MARCADORES = {
    "<NOMBRE_EMPRESA>": "Rut Soc A",
    "<RUT_SOCIEDAD>": "RUT_SOCIEDAD",
    "<REPRESENTANTE_LEGAL>": "REPRESENTANTE_LEGAL",
    "<INTERESES>": "INTERESES",
    "<NOMBRE_EJEMPLO>": "NOMBRE_EJEMPLO",
}
