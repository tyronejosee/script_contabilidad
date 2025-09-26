# 💵 **Análisis de Cheques en Excel**

Este script procesa un archivo **Excel**, lo divide en secciones según un **separador específico**, filtra y transforma los datos. Extrae información relevante como **códigos, nombres y fechas**, elimina datos innecesarios y exporta la información procesada en un nuevo archivo Excel, limpiando archivos temporales al finalizar.

## 💻 **Comandos**

Ejecutar el script:

```bash
python main.py
```

## ⚙️ **Configuración**

* 📄 **Archivo de entrada**: `input.xlsx`
* 📑 **Hoja esperada**: `Softland`
* 📂 **Archivo de salida**: `output.xlsx` (se genera automáticamente)

## 📥 **Estructura esperada del Excel**

Ejemplo de los datos que debe contener la hoja **"Softland"**:

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

## 📤 **Archivos generados**

El script crea un nuevo archivo **procesado** con la información filtrada y modificada.

Ejemplo:

```bash
output.xlsx
```

## 🔍 **Validaciones incluidas**

✔️ Verifica que el archivo de entrada exista.
✔️ Confirma que la hoja `"Softland"` esté presente.
✔️ Chequea la estructura mínima de los datos.
✔️ Elimina datos temporales una vez finalizado el proceso.

## ✅ **Resultado Final**

| **Código** | **Nombre**     | **Fecha Emisión** | **Fecha Vencimiento** | **Tipo** | **Número** | **Monto** | **Descripción**                       | **Saldo** |
| ---------- | -------------- | ----------------- | --------------------- | -------- | ---------- | --------- | ------------------------------------- | --------- |
| 20012345   | FALSECIO REYES | 15-06-2023        | 20-01-2025            | CH       | 123,456    | 750,300   | Pago de documento anticipo: CH 123456 | 0         |
| 20012345   | FALSECIO REYES | 15-06-2023        | 20-02-2025            | CH       | 123,457    | 750,300   | Pago de documento anticipo: CH 123457 | 0         |
| 20012345   | FALSECIO REYES | 15-06-2023        | 20-03-2025            | CH       | 123,458    | 750,300   | Pago de documento anticipo: CH 123458 | 0         |
