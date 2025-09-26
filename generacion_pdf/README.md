# 📄 **Generador de PDFs desde Excel**

Este script permite generar automáticamente documentos **PDF personalizados** a partir de un archivo **Excel** y una plantilla **PDF base**. El flujo consiste en cargar datos desde Excel, insertar información en posiciones definidas dentro del PDF, y exportar un archivo por cada fila del Excel.

Incluye guías de depuración (líneas rojas y grises) para ayudar a ubicar los campos en el diseño.

## 💻 **Comandos**

Ejecutar el script:

```bash
python main.py
````

## ⚙️ **Configuración**

* 📊 **Archivo de datos (Excel)**: `input.xlsx` (Contiene la información de los usuarios que será inyectada en los PDFs).
* 📝 **Plantilla PDF**: `template.pdf` (Documento base donde se insertarán los datos en coordenadas específicas).
* 📂 **Carpeta de salida**: `output/` (Lugar donde se guardarán los PDFs generados automáticamente).

### 🔠 **Fuentes disponibles** (ejemplos)

* Helvetica, Helvetica-Bold, Helvetica-Oblique
* Times-Roman, Times-Bold, Times-Italic
* Courier, Courier-Bold, Courier-Oblique
* Symbol, ZapfDingbats

### 📐 **Constantes configurables** en `constants.py`

   ```python
   INPUT_FILE = "input.xlsx"
   TEMPLATE_PDF = "template.pdf"
   OUTPUT_DIR = "output"
   LINES = True         # Mostrar líneas guía
   FONT_TYPE = "Helvetica"
   FONT_SIZE = 11
   PAGE_SIZE = letter
   GUIDE_INTERVAL = 50
   ```

## 📥 **Excel de Entrada**

Ejemplo de estructura del archivo `input.xlsx`:

| Nombre | Apellido | Edad |
| ------ | -------- | ---- |
| Juan   | Pérez    | 28   |
| María  | González | 34   |
| Pedro  | López    | 41   |

Cada fila representa un registro que se transformará en un **PDF individual**.

## 📤 **PDFs Generados**

Por cada fila del Excel se generará un archivo en la carpeta `output/` con el nombre:

```bash
Nombre Apellido.pdf
```

Ejemplo:

* `Juan Pérez.pdf`
* `María González.pdf`
* `Pedro López.pdf`

## 🎨 **Modo Guías (Opcional)**

Si `LINES = True`, el script dibujará una grilla con:

* 🔴 Líneas rojas cada 100px
* ⚪ Líneas grises cada 10px

Esto facilita ajustar las posiciones exactas del texto en la plantilla PDF.

## ✅ **Resultado Final**

* Carga datos desde Excel.
* Inserta información en un PDF base en posiciones predefinidas.
* Exporta un PDF por cada registro.
* Muestra mensajes de estado durante el proceso.
