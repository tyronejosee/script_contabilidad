# 📊 **Generador de Reportes Financieros**

Este script genera un **reporte financiero automatizado** a partir de datos de ejemplo. Produce un **resumen en Excel**, un **gráfico en PNG** y un **reporte consolidado en PDF** que combina estadísticas y visualizaciones.

## 💻 **Comandos**

Ejecutar el script:

```bash
python main.py
````

## ⚙️ **Flujo del Script**

### 📝 **Generación de datos**

   Se crean datos simulados con fechas, conceptos (Ingresos/Egresos) y montos.

### 📊 **Resumen**

   Se agrupan los datos por concepto (`Ingreso`, `Egreso`) y se calcula la suma de montos.

### 📂 **Exportación de resultados**

* **Excel** → `output.xlsx` con el resumen.
* **Gráfico** → `grafico_ingresos_egresos.png` con barras de ingresos (verde) y egresos (rojo).
* **PDF** → `reporte_completo.pdf` con el gráfico embebido.

## 📥 **Datos de Ejemplo**

El script genera un DataFrame con la siguiente estructura:

| Fecha      | Concepto | Monto  |
| ---------- | -------- | ------ |
| 2024-01-01 | Ingreso  | 100000 |
| 2024-01-02 | Egreso   | 50000  |
| 2024-01-03 | Ingreso  | 200000 |
| 2024-01-04 | Egreso   | 30000  |
| 2024-01-05 | Ingreso  | 150000 |

## 📤 **Archivos de Salida**

* `output.xlsx` → Resumen financiero por concepto.
* `grafico_ingresos_egresos.png` → Visualización en barras.
* `reporte_completo.pdf` → Documento final con el gráfico integrado.

## 🎨 **Visualización Generada**

El gráfico de barras diferencia los conceptos por color:

* 🟩 **Ingresos** → Verde
* 🟥 **Egresos** → Rojo

## ✅ **Resultado Final**

* Genera automáticamente **datos financieros de prueba**.
* Calcula un **resumen agrupado**.
* Exporta en **Excel, PNG y PDF**.
* Útil como plantilla para proyectos de **contabilidad, análisis financiero o dashboards**.
