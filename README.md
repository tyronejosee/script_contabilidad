# 🧰 Script Contabilidad

Este repositorio es un **conjunto de herramientas automatizadas en Python** diseñadas para optimizar tareas comunes en contabilidad, análisis financiero y generación de documentos. Cada módulo es independiente y resuelve un problema específico, pero todos comparten un enfoque en la **automatización de flujos repetitivos basados en archivos Excel, Word y PDF**.

## ⚙️ Instalación

Clona el repositorio y navega a la carpeta.

```bash
git clone git@github.com:tyronejosee/script_contabilidad.git
cd script_contabilidad
```

Instala las dependencias y crea el ambiente virtual.

> Recomendamos usar [uv](https://docs.astral.sh/uv/guides/install-python/#getting-started).

```bash
uv sync
```

Si necesitas crear un ejecutable, empaqueta tu script.

```bash
cd <nombre-modulo>
uv run pyinstaller --onefile <nombre-script>.py
```

Esto genera.

* Un ejecutable `.exe` en la carpeta `dist/` del modulo.
* Carpeta `build/` con archivos temporales del modulo.
* Archivo `.spec` (configurable si necesitas personalización).

Opciones útiles.

* `--onefile`: todo en un solo `.exe`.
* `--noconsole`: para apps con GUI (no abre consola).
* `--icon=icono.ico`: asigna un ícono.

Ejemplo completo.

```bash
uv run pyinstaller --onefile --icon=<nombre-icono>.ico <nombre-script>.py
```

## 🗂️ Estructura del Proyecto

Cada carpeta es un módulo ejecutable con su propio `main.py` y un `README.md` explicando su uso.

```bash
agrupacion_odoo/               # Divide libro mayor en múltiples archivos por cuenta
analisis_cheques/              # Analiza y filtra cheques desde archivos Excel
analitica_proveedores/         # Limpia y netea análisis de proveedores (versión Kame)
analitica_provedores_odoo/     # Variante para análisis de proveedores desde Odoo
generacion_contratos/          # Genera documentos Word y los convierte a PDF
generacion_pdf/                # Inserta datos en plantillas PDF desde Excel
generacion_reportes/           # Crea reportes financieros y gráficos automáticamente
txt_softland/                  # Procesa extractos bancarios para exportar a TXT Softland
unir_excels_banco_estado/      # Une y consolida múltiples archivos Excel bancarios
```

## 📁 Estructura Típica de un Script

Cada módulo sigue un patrón similar:

* `constants.py` → Configuraciones y variables globales
* `main.py` → Script ejecutable principal
* `README.md` → Guía específica del módulo
* `output/` → Carpeta donde se generan los archivos procesados (Opcional)

---

## 📦 Scripts Disponibles

### Agrupación de Libro Mayor (`agrupacion_odoo/`)

Divide un archivo Excel del libro mayor en múltiples archivos, uno por cada cuenta contable.

```bash
cd agrupacion_odoo
python main.py
```

### Análisis de Cheques (`analisis_cheques/`)

Procesa un Excel con datos bancarios, filtra secciones relevantes y genera un nuevo archivo limpio.

```bash
cd analisis_cheques
python main.py
```

### Analítica de Proveedores (`analitica_proveedores/` y `analitica_provedores_odoo/`)

Limpia informes de proveedores exportados desde sistemas contables (Kame u Odoo), netea saldos y genera un Excel consolidado.

```bash
cd analitica_proveedores
python main.py
```

### Generación Automática de Contratos (`generacion_contratos/`)

Toma datos desde Excel y los inserta en plantillas Word para generar contratos, luego los convierte a PDF.

```bash
cd generacion_contratos
python main.py
```

💡 Requiere tener instalado **LibreOffice** para la conversión automática a PDF.

### Generación de PDFs Personalizados (`generacion_pdf/`)

Inserta datos desde Excel en posiciones específicas de una plantilla PDF y genera documentos individuales.

```bash
cd generacion_pdf
python main.py
```

### Reportes Financieros Automatizados (`generacion_reportes/`)

Crea un resumen financiero, genera gráficos y exporta todo en Excel, PNG y PDF.

```bash
cd generacion_reportes
python main.py
```

### TXT Softland (`txt_softland/`)

Convierte extractos bancarios Excel en archivos limpios y listos para ser importados en **Softland**.

```bash
cd txt_softland
python main.py
```

---

## ⚖️ Licencia

Este proyecto está licenciado bajo la [Apache 2.0](LICENSE).
