# **Unir Excels Banco Estado**

Este script ayuda a combinar varios archivos de Excel en uno solo de manera sencilla. Primero, permite ver qué archivos de Excel hay en la carpeta. Luego, el usuario elige una hoja específica de estos archivos y el programa combina sus datos en un nuevo archivo. Si todo sale bien, guarda el resultado en un nuevo archivo de Excel. También muestra mensajes de estado en colores para que sea fácil de entender.

## **Comandos**

Ejecutar el script.

```bash
python main.py
```

## **Excels Entrada**

Secuencia númerica de excels

- [x] **Nombre Archivo**: `100.xlsx`
- [x] **Nombre Tabla**: `Movimientos`

| **Fecha**  | **Sucursal** | **N° Cuenta Corriente** | **Alias**                 | **N° Cartola** | **N° Operación** | **Descripción**                   | **Cheques / Cargos** | **Depósitos / Abonos** | **Saldo**   |
| ---------- | ------------ | ----------------------- | ------------------------- | -------------- | ---------------- | --------------------------------- | -------------------- | ---------------------- | ----------- |
| 10/01/2025 | Valparaíso   | 01456789012             | INMOBILIARIA DEL MAR LTDA | 205            | 0001054          | Cheque recibido en canje de banco | $150,250             | $0                     | $15,302,150 |
| 10/01/2025 | Valparaíso   | 01456789012             | INMOBILIARIA DEL MAR LTDA | 205            | 0001062          | Transferencia desde otro banco    | $0                   | $2,500,000             | $17,802,150 |
| 10/01/2025 | Stgo. Centro | 01456789012             | INMOBILIARIA DEL MAR LTDA | 205            | 7018990          | Pago de impuestos                 | $1,200,000           | $0                     | $16,602,150 |

- [x] **Nombre Archivo**: `101.xlsx`
- [x] **Nombre Tabla**: `Movimientos`

| **Fecha**  | **Sucursal** | **N° Cuenta Corriente** | **Alias**                  | **N° Cartola** | **N° Operación** | **Descripción**                   | **Cheques / Cargos** | **Depósitos / Abonos** | **Saldo**   |
| ---------- | ------------ | ----------------------- | -------------------------- | -------------- | ---------------- | --------------------------------- | -------------------- | ---------------------- | ----------- |
| 15/02/2025 | Concepción   | 02578945623             | CONSTRUCCIONES DEL SUR SPA | 312            | 0002078          | Cheque recibido en canje de banco | $500,000             | $0                     | $8,750,000  |
| 15/02/2025 | Concepción   | 02578945623             | CONSTRUCCIONES DEL SUR SPA | 312            | 0002083          | Transferencia interna             | $0                   | $3,000,000             | $11,750,000 |
| 15/02/2025 | Temuco       | 02578945623             | CONSTRUCCIONES DEL SUR SPA | 312            | 5023471          | Pago de proveedores               | $1,800,000           | $0                     | $9,950,000  |

- [x] **Nombre Archivo**: `102.xlsx`
- [x] **Nombre Tabla**: `Movimientos`

| **Fecha**  | **Sucursal** | **N° Cuenta Corriente** | **Alias**                    | **N° Cartola** | **N° Operación** | **Descripción**      | **Cheques / Cargos** | **Depósitos / Abonos** | **Saldo**  |
| ---------- | ------------ | ----------------------- | ---------------------------- | -------------- | ---------------- | -------------------- | -------------------- | ---------------------- | ---------- |
| 20/03/2025 | Antofagasta  | 03698712345             | SERVICIOS MINEROS NORTE LTDA | 417            | 0003092          | Depósito en efectivo | $0                   | $1,200,000             | $5,600,000 |
| 20/03/2025 | Antofagasta  | 03698712345             | SERVICIOS MINEROS NORTE LTDA | 417            | 0003098          | Cheque emitido       | $350,000             | $0                     | $5,250,000 |
| 20/03/2025 | Copiapó      | 03698712345             | SERVICIOS MINEROS NORTE LTDA | 417            | 8035673          | Pago de facturas     | $1,500,000           | $0                     | $3,750,000 |

## **Excel Salida**

Todos los excels de la tabla `Movimientos` unidos en un solo documento.

- [x] **Nombre Archivo**: `output.xlsx` (Definido por el usuario)
- [x] **Nombre Tabla**: `Sheet1`

| **Fecha**  | **Sucursal** | **N° Cuenta Corriente** | **Alias**                   | **N° Cartola** | **N° Operación** | **Descripción**                                                    | **Cheques / Cargos** | **Depósitos / Abonos** | **Saldo**   |
| ---------- | ------------ | ----------------------- | --------------------------- | -------------- | ---------------- | ------------------------------------------------------------------ | -------------------- | ---------------------- | ----------- |
| 03/12/2024 | Stgo. Centro | 1,450,987,654           | INGENIERÍA DEL PACÍFICO SPA | 150            | 8,123,456        | Transferencia bancoestado a rut 17234567-8 Muñoz Herrera Ana María | $420,315             | $0                     | $18,750,890 |
| 05/12/2024 | Valparaíso   | 1,450,987,654           | INGENIERÍA DEL PACÍFICO SPA | 151            | 23               | Cheque recibido en canje de banco                                  | $310,200             | $0                     | $19,061,090 |
| 06/12/2024 | Concepción   | 1,450,987,654           | INGENIERÍA DEL PACÍFICO SPA | 151            | 45               | Cheque recibido en canje de banco                                  | $275,890             | $0                     | $19,336,980 |
