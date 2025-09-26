# 📊 **Procesador de Libro Mayor en Excel**

Este script toma un archivo **Excel** que contiene la hoja `"Libro mayor"`, valida su estructura y lo divide en **archivos separados por cuenta contable**. Cada cuenta se exporta como un nuevo Excel dentro de la carpeta `output/`.

## 💻 **Comandos**

Ejecutar el script:

```bash
python main.py
````

## ⚙️ **Configuración**

* 📄 **Archivo de entrada**: `input.xlsx`
* 📑 **Hoja esperada**: `Libro mayor`
* 📂 **Carpeta de salida**: `output/` (se crea automáticamente)
* 📌 **Columnas obligatorias** que deben existir en el archivo:

  ```text
  Código
  Nombre de la cuenta
  Fecha
  Comunicación
  Empresa
  Moneda
  Debe
  Haber
  Balance
  ```

## 📥 **Estructura esperada del Excel**

Ejemplo de cómo debe lucir la hoja **"Libro mayor"**:

| Código | Nombre de la cuenta | Fecha      | Comunicación | Empresa | Moneda | Debe   | Haber | Balance |
| ------ | ------------------- | ---------- | ------------ | ------- | ------ | ------ | ----- | ------- |
| 1001   | Caja Principal      | 01/01/2025 | Comprobante1 | ACME    | CLP    | 100000 |       | 100000  |
|        |                     | 02/01/2025 | Comprobante2 | ACME    | CLP    |        | 20000 | 80000   |
| Total  | Caja Principal      |            |              |         |        |        |       | 80000   |
| 1002   | Banco               | 01/01/2025 | Comprobante3 | ACME    | CLP    | 50000  |       | 50000   |
|        |                     | 03/01/2025 | Comprobante4 | ACME    | CLP    |        | 15000 | 35000   |
| Total  | Banco               |            |              |         |        |        |       | 35000   |

## 📤 **Archivos generados**

El script divide automáticamente el libro mayor y genera un archivo **Excel por cada cuenta** en la carpeta `output/`.

Ejemplo de nombres de archivos generados:

```bash
1001_Caja Principal.xlsx
1002_Banco.xlsx
```

## 🔍 **Validaciones incluidas**

✔️ Verifica que el archivo exista.
✔️ Confirma que la hoja `"Libro mayor"` esté presente.
✔️ Chequea que las **columnas obligatorias** estén incluidas.
✔️ Detecta si la hoja está vacía.
✔️ Limpia los nombres de archivo eliminando caracteres inválidos.

## ✅ **Resultado Final**

```bash
🔄 Procesando archivo: '1001_Caja Principal.xlsx'
🔄 Procesando archivo: '1002_Banco.xlsx'

✅ 2 archivos generados en la carpeta `output/`.
```
