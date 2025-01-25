# **Analitica Proveedores**

Limpia el analisis de proveedores de Kame y netea folios pagados.

## **Comandos**

Ejecutar el script.

```bash
python main.py
```

Ejecutar el plot luego de generar el `output.xlsx`.

```bash
python plotting.py
```

## **Excel Entrada**

- [x] **Nombre Archivo**: `input.xlsx`
- [x] **Nombre Tabla**: `id`

| Ficha                          | Fecha      | Tipo Doc.           | Número    | Abonos $ | Cargos $ | Saldo $  |
| ------------------------------ | ---------- | ------------------- | --------- | -------- | -------- | -------- |
| 12.345.678-9 EMPRESA ABC LTDA. | 10/03/2024 | Factura Electrónica | 1,234,567 | 500,000  | 0        | -500,000 |
| 98.765.432-1 NEGOCIOS XYZ SPA  | 22/07/2023 | Nota de Crédito     | 56,789    | 200,000  | 200,000  | 0        |
| 76.543.210-5 SOLUCIONES LM SA  | 15/11/2024 | Factura Electrónica | 78,910    | 0        | 50,000   | 50,000   |

## **Excel Salida**

- [x] **Nombre Archivo**: `output.xlsx`
- [x] **Nombre Tabla**: `Sheet1`

| Ficha                          | Fecha      | Tipo Doc.           | Número    | Abonos $ | Cargos $ | Saldo $  | Saldo Absoluto |
| ------------------------------ | ---------- | ------------------- | --------- | -------- | -------- | -------- | -------------- |
| 12.345.678-9 EMPRESA ABC LTDA. | 10/03/2024 | Factura Electrónica | 1,234,567 | 500,000  | 0        | -500,000 | 500,000        |
| 98.765.432-1 NEGOCIOS XYZ SPA  | 22/07/2023 | Nota de Crédito     | 56,789    | 200,000  | 200,000  | 0        | 0              |
| 76.543.210-5 SOLUCIONES LM SA  | 15/11/2024 | Factura Electrónica | 78,910    | 0        | 50,000   | 50,000   | 50,000         |

## **Variables**

Revisa el archivo `contants.py` para verificar los parámetros del documento.

```python
# constants.py

NOMBRE_HOJA = "id"
```
