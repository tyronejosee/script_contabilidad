# **Análisis Cheques**

Este script toma un archivo de Excel, lo divide en secciones según un separador específico y luego filtra y modifica los datos. Extrae información relevante, como códigos y nombres, convierte fechas al formato adecuado y elimina datos innecesarios. Finalmente, guarda la información procesada en un nuevo archivo de Excel y limpia archivos temporales.

## **Comandos**

Ejecutar el script.

```bash
python main.py
```

## **Excel Entrada**

- [x] **Nombre Archivo**: `input.xlsx`
- [x] **Nombre Tabla**: `Softland`

| **Campo**           | **Valor**         |
| ------------------- | ----------------- |
| **Código**          | 12345678          |
| **Nombre**          | Yo Mismo Tu Mismo |
| **Dirección**       | Calle Falsa 123   |
| **Comuna**          | Comuna Ficticia   |
| **Teléfonos**       | +1234567890       |
| **Ciudad**          | Ciudad Imaginaria |
| **Fax**             | +0987654321       |
| **Contacto**        | Doña Falsa        |
| **Vendedor**        | Falsacio Reyes    |
| **Cobrador**        | Hector Falseto    |
| **Crédito**         | 5000              |
| **Área de Negocio** | GLOBAL            |

---

| **Documento** | **Fecha Emisión** | **Fecha Vcto** | **Tipo** | **N°** | **Correlativo** | **Cpbte Doc. compra** | **Cpbte** | **Debe** | **Haber** | **Saldo** | **Descripción**                       |
| ------------- | ----------------- | -------------- | -------- | ------ | --------------- | --------------------- | --------- | -------- | --------- | --------- | ------------------------------------- |
| 1-1-04-003    |                   |                |          |        |                 |                       |           |          |           |           | CHEQUES EN CARTERA                    |
| CH            | 6/15/2024         | 7/15/2024      | CH       | 987654 | 123             | 500,000               |           | 500,000  |           | 500,000   | Pago de documento anticipo: CH 987654 |
| CH            | 6/20/2024         | 7/20/2024      | CH       | 987655 | 123             | 400,000               |           | 400,000  |           | 400,000   | Pago de documento anticipo: CH 987655 |
| CH            | 6/25/2024         | 7/25/2024      | CH       | 987656 | 123             | 300,000               |           | 300,000  |           | 300,000   | Pago de documento anticipo: CH 987656 |
| CH            | 7/1/2024          | 8/1/2024       | CH       | 987657 | 123             | 200,000               |           | 200,000  |           | 200,000   | Pago de documento anticipo: CH 987657 |
| CH            | 7/5/2024          | 8/5/2024       | CH       | 987658 | 123             | 100,000               |           | 100,000  |           | 100,000   | Pago de documento anticipo: CH 987658 |

---

| **Total** | **Cheque** | **Monto Total** |
| --------- | ---------- | --------------- |
|           | CHEQUE     | 1,500,000       |

## **Excel Salida**

- [x] **Nombre Archivo**: `output.xlsx`
- [x] **Nombre Tabla**: `Sheet1`

| **Código** | **Nombre**     | **Fecha Emisión** | **Fecha Vencimiento** | **Tipo** | **Número** | **Monto** | **Descripción**                       | **Saldo** |
| ---------- | -------------- | ----------------- | --------------------- | -------- | ---------- | --------- | ------------------------------------- | --------- |
| 20012345   | FALSECIO REYES | 15-06-2023        | 20-01-2025            | CH       | 123,456    | 750,300   | Pago de documento anticipo: CH 123456 | 0         |
| 20012345   | FALSECIO REYES | 15-06-2023        | 20-02-2025            | CH       | 123,457    | 750,300   | Pago de documento anticipo: CH 123457 | 0         |
| 20012345   | FALSECIO REYES | 15-06-2023        | 20-03-2025            | CH       | 123,458    | 750,300   | Pago de documento anticipo: CH 123458 | 0         |

## **Variables**

Revisa el archivo `contants.py` para verificar los parámetros del documento.

```python
# constants.py

SHEET_NAME = "Softland"
```
