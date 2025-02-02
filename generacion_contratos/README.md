# **Generación Contratos**

## **Comandos**

Ejecutar el script.

```bash
python main.py
```

## **Configuración**

1. Instala `LibreOffice` desde [aquí](https://es.libreoffice.org/descarga/libreoffice/). Esta aplicación hará la conversion de word a pdf

2. Asegúrate de contar con dos archivos de entrada:

   - **Archivo de datos (Excel)**: `input.xlsx`
   - **Plantila Word**: `template.docx`

3. Dentro de template.docx, inserta llaves en el formato `<FORMATO_LLAVE>` en los lugares donde necesites reemplazar el texto. Asegúrate de mantener los espacios adecuados entre las llaves y el resto del párrafo para evitar errores en el reemplazo.

4. Define la relación entre las llaves del documento Word y las columnas del archivo Excel dentro de `constants.py`.

   ```python
   PLACEHOLDERS = {
       "<FORMATO_LLAVE>": "Columna de Excel",
   }
   ```

## **Constantes**

Verifica el archivo `constants.py` para asegurarte de que los parámetros del documento estén correctamente configurados.

```python
# constants.py

# Archivo de entrada con los datos para el reemplazo.
INPUT_FILE = "input.xlsx"

# Plantilla base utilizada para la generación de documentos.
TEMPLATE_FILE = "template.docx"

# Columna en el archivo Excel que se usará para nombrar los archivos generados.
OUTPUT_FIELD = "NOMBRE_EMPRESA"

# Carpeta donde se guardarán los documentos generados.
OUTPUT_FOLDER = "output"

# Fuente que se aplicará al texto formateado. Asegúrate de que coincida con la fuente del documento.
FONT_TYPE = "Calibri"

# Tamaño de fuente a aplicar en el texto formateado.
FONT_SIZE = 11
```
