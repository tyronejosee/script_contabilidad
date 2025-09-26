# 📑 **Analítica de Proveedores en Excel**

Este script limpia el **análisis de proveedores** exportado desde **Kame** y **netea folios pagados**, dejando un consolidado listo para análisis y visualización.

## 💻 **Comandos**

Ejecutar el script principal:

```bash
python main.py
```

Generar el gráfico luego de producir `output.xlsx`:

```bash
python plotting.py
```

## ⚙️ **Configuración**

* 📄 **Archivo de entrada**: `input.xlsx`
* 📑 **Hoja esperada**: `id`
* 📂 **Archivo de salida**: `output.xlsx`

## 📥 **Estructura esperada del Excel**

Ejemplo de datos en la hoja **"id"**:

| Ficha                          | Fecha      | Tipo Doc.           | Número    | Abonos $ | Cargos $ | Saldo $  |
| ------------------------------ | ---------- | ------------------- | --------- | -------- | -------- | -------- |
| 12.345.678-9 EMPRESA ABC LTDA. | 10/03/2024 | Factura Electrónica | 1,234,567 | 500,000  | 0        | -500,000 |
| 98.765.432-1 NEGOCIOS XYZ SPA  | 22/07/2023 | Nota de Crédito     | 56,789    | 200,000  | 200,000  | 0        |
| 76.543.210-5 SOLUCIONES LM SA  | 15/11/2024 | Factura Electrónica | 78,910    | 0        | 50,000   | 50,000   |

## 📤 **Archivos generados**

El script crea un archivo procesado con la información depurada:

```bash
output.xlsx
```

## 🔍 **Validaciones incluidas**

✔️ Verifica que el archivo de entrada exista.
✔️ Confirma que la hoja `"id"` esté presente.
✔️ Calcula el **saldo absoluto**.
✔️ Netea los folios ya pagados.

## ✅ **Resultado Final**

| Ficha                          | Fecha      | Tipo Doc.           | Número    | Abonos $ | Cargos $ | Saldo $  | Saldo Absoluto |
| ------------------------------ | ---------- | ------------------- | --------- | -------- | -------- | -------- | -------------- |
| 12.345.678-9 EMPRESA ABC LTDA. | 10/03/2024 | Factura Electrónica | 1,234,567 | 500,000  | 0        | -500,000 | 500,000        |
| 98.765.432-1 NEGOCIOS XYZ SPA  | 22/07/2023 | Nota de Crédito     | 56,789    | 200,000  | 200,000  | 0        | 0              |
| 76.543.210-5 SOLUCIONES LM SA  | 15/11/2024 | Factura Electrónica | 78,910    | 0        | 50,000   | 50,000   | 50,000         |
