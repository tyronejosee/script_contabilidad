# 📊 **TXT Softland**

Este script permite procesar archivos de datos bancarios en formato Excel, donde el usuario selecciona el banco, ingresa las rutas de archivo de entrada y salida, y el script transforma y limpia los datos, renombrando columnas, agregando año a las fechas, generando columnas autoincrementales, creando descripciones cortas y convirtiendo los montos en valores numéricos. Después de procesar y ajustar los datos según las configuraciones del banco, guarda el archivo procesado en la ruta de salida proporcionada por el usuario.

## 💻 **Comandos**

Ejecutar el script.

```bash
python main.py
````

## 📥 **Excel Entrada**

### 📑 **Nombre Archivo**: `bci.xlsx`

| Fecha      | Sucursal  | Descripción                             | N° Documento | Cheques y otros cargos | Depósitos y Abono | Saldo diario |
| ---------- | --------- | --------------------------------------- | ------------ | ---------------------- | ----------------- | ------------ |
| 02/12/2024 | OF VIRT U | PAGO RECIBIDO TF2 096689310-9 TRANSBANK | 123456       | 200,000                | 1,500,000         | 3,000,000    |
| 02/12/2024 | OF CENTRA | TRANSFERENCIA DE FONDOS AUTOSERVICIO    | 987654321    | 5,000,000              | 6,500,000         | 8,000,000    |
| 02/12/2024 | IQUIQUE   | DEPOSITO CHEQUE/DOCUMENTO BCI           | 654321       | 450,000                | 2,000,000         | 4,500,000    |

### 📑 **Nombre Archivo**: `chile.xlsx`

| Fecha     | Detalle Movimiento              | Cheque o Cargo | Deposito o Abono | Saldo     | Docto. Nro. | Trn | Caja | Sucursal    |
| --------- | ------------------------------- | -------------- | ---------------- | --------- | ----------- | --- | ---- | ----------- |
| 12/2/2024 | CHEQUE PAGADO POR CAJA          | 1,500,000      | 0                | 750,000   | 12345       | 0   | 0    | OF. IQUIQUE |
| 12/2/2024 | DEPOSITO CON CHEQUE MISMO BANCO | 0              | 600,000          | 1,200,000 | 54321       | 0   | 0    | OF. IQUIQUE |
| 12/2/2024 | DEP.CHEQ.OTROS BANCOS           | 0              | 1,000,000        | 2,500,000 | 67890       | 0   | 0    | OF. IQUIQUE |

### 📑 **Nombre Archivo**: `estado.xlsx`

| Fecha      | Sucursal       | N° Cuenta Corriente | Alias                 | N° Cartola | N° Operación | Descripción                                       | Cheques / Cargos | Depósitos / Abonos | Saldo      |
| ---------- | -------------- | ------------------- | --------------------- | ---------- | ------------ | ------------------------------------------------- | ---------------- | ------------------ | ---------- |
| 02/12/2024 | Stgo.principal | 1,234,567,890       | CONSTRUCTORA TRES SPA | 99         | 8,000,000    | Transferencia Banco XYZ a rut 11223344-5 Gonzalez | 500,000          | 0                  | 15,000,000 |
| 04/12/2024 | Iquique        | 1,234,567,890       | CONSTRUCTORA TRES SPA | 100        | 15           | Cheque recibido en canje de Banco ABC             | 150,000          | 0                  | 18,000,000 |
| 04/12/2024 | Iquique        | 1,234,567,890       | CONSTRUCTORA TRES SPA | 100        | 18           | Cheque recibido en canje de Banco ABC             | 200,000          | 0                  | 19,000,000 |

### 📑 **Nombre Archivo**: `itau.xlsx`

| Fecha | Número de operación | Sucursal | Descripción                  | Depósitos o abonos | Giros o cargos | Saldo diario |
| ----- | ------------------- | -------- | ---------------------------- | ------------------ | -------------- | ------------ |
| 02/12 | 123456789           | 1980     | Transferencia De Juan Pérez  | $3,000,000         | $0             | $7,500,000   |
| 02/12 | 987654321           | 0172     | Cheque Pagado Caja           | $0                 | $2,500,000     | $4,200,000   |
| 02/12 | 112233445           | 0172     | Dep.doc. Otros Bancos/48 Hrs | $800,000           | $0             | $5,100,000   |

### 📑 **Nombre Archivo**: `scotiabank.xlsx`

| Fecha      | Descripción             | Numero Documento | Cargo | Abono   | Saldo Diario |
| ---------- | ----------------------- | ---------------- | ----- | ------- | ------------ |
| 02-12-2024 | DEPOSITO CON DOCUMENTOS | 1,123,456        | 0     | 800,000 | 20,000,000   |
| 02-12-2024 | DEPOSITO CON DOCUMENTOS | 1,123,457        | 0     | 300,000 | 20,300,000   |
| 02-12-2024 | DEPOSITO CON DOCUMENTOS | 1,123,458        | 0     | 250,000 | 20,550,000   |

## 📤 **Excel Salida**

### 📑 **Nombre Archivo**: `output.xlsx`

| INDEX | FECHA      | DESCRIPCION | N_DOCUMENTO | CHEQUES_CARGOS | DEPOSITOS_ABONOS |
| ----- | ---------- | ----------- | ----------- | -------------- | ---------------- |
| 1     | 02/12/2024 | CB          | 7,123,456   | 350,000        | 0                |
| 2     | 04/12/2024 | CH          | 12          | 290,000        | 0                |
| 3     | 04/12/2024 | CH          | 17          | 310,000        | 0                |
