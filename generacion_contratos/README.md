# 📄 **Generación de Contratos**

Este script permite generar automáticamente documentos **Word** personalizados a partir de un archivo **Excel** y una plantilla **Word base**, y luego convertirlos a **PDF** usando LibreOffice.

## 💻 **Comandos**

Ejecutar el script:

```bash
python main.py
````

## ⚙️ **Configuración**

* Instala `LibreOffice` desde [aquí](https://es.libreoffice.org/descarga/libreoffice/). Esta aplicación realizará la conversión de Word a PDF
* Asegúrate de contar con dos archivos de entrada
  * 📊 **Archivo de datos (Excel)**: `input.xlsx`
  * 📝 **Plantilla Word**: `template.docx`
* Dentro de `template.docx`, inserta llaves en el formato `<FORMATO_LLAVE>` en los lugares donde necesites reemplazar el texto. Mantén los espacios adecuados entre las llaves y el resto del párrafo para evitar errores en el reemplazo
* Define la relación entre las llaves del documento Word y las columnas del archivo Excel dentro de `constantes.py`

## 🔧 **Constantes**

Verifica el archivo `constantes.py` para asegurarte de que los parámetros del documento estén correctamente configurados:

```python
# constantes.py

# Archivo de entrada con los datos para el reemplazo.
ARCHIVO_ENTRADA = "input.xlsx"

# Plantilla base utilizada para la generación de documentos.
PLANTILLA_DOCX = "template.docx"

# Columna en el archivo Excel que se usará para nombrar los archivos generados.
CAMPO_SALIDA = "NOMBRE_EMPRESA"

# Carpeta donde se guardarán los documentos generados.
CARPETA_SALIDA = "output"

# Fuente que se aplicará al texto formateado. Asegúrate de que coincida con la fuente del documento.
TIPO_FUENTE = "Calibri"

# Tamaño de fuente a aplicar en el texto formateado.
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
```

## ✅ **Flujo del Script**

1. Carga los datos desde el Excel (`ARCHIVO_ENTRADA`).
2. Reemplaza los marcadores en la plantilla Word (`PLANTILLA_DOCX`) según `MARCADORES`.
3. Genera un documento Word por cada fila del Excel en `CARPETA_SALIDA`.
4. Convierte automáticamente los documentos Word generados a PDF usando LibreOffice.
5. Muestra mensajes de progreso en consola indicando los documentos creados y convertidos.
