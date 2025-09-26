# Constants
ANIO_MUESTRA = 2024
CONFIG_BANCOS = {
    "Banco Estado": {
        "renombrar_columnas": {
            "Fecha": "FECHA",
            "N° Operación": "N_DOCUMENTO",
            "Descripción": "DESCRIPCION",
            "Cheques / Cargos": "CHEQUES_CARGOS",
            "Depósitos / Abonos": "DEPOSITOS_ABONOS",
        },
        "columnas_salida": [
            "INDEX",
            "FECHA",
            "DESCRIPCION",
            "N_DOCUMENTO",
            "CHEQUES_CARGOS",
            "DEPOSITOS_ABONOS",
        ],
        "columnas_numericas": [
            "Cheques / Cargos",
            "Depósitos / Abonos",
        ],
    },
    "Banco BCI": {
        "renombrar_columnas": {
            "Fecha": "FECHA",
            "N° Documento": "N_DOCUMENTO",
            "Descripción": "DESCRIPCION",
            "Cheques y otros cargos": "CHEQUES_CARGOS",
            "Depósitos y Abono": "DEPOSITOS_ABONOS",
        },
        "columnas_salida": [
            "INDEX",
            "FECHA",
            "DESCRIPCION",
            "N_DOCUMENTO",
            "CHEQUES_CARGOS",
            "DEPOSITOS_ABONOS",
        ],
        "columnas_numericas": [
            "Cheques y otros cargos",
            "Depósitos y Abono",
        ],
    },
    "Banco Itaú": {
        "renombrar_columnas": {
            "Fecha": "FECHA",
            "Sucursal": "N_DOCUMENTO",
            "Descripción": "DESCRIPCION",
            "Giros o cargos": "CHEQUES_CARGOS",
            "Depósitos o abonos": "DEPOSITOS_ABONOS",
        },
        "columnas_salida": [
            "INDEX",
            "FECHA",
            "DESCRIPCION",
            "N_DOCUMENTO",
            "CHEQUES_CARGOS",
            "DEPOSITOS_ABONOS",
        ],
        "columnas_numericas": [
            "Giros o cargos",
            "Depósitos o abonos",
        ],
    },
    "Banco de Chile": {
        "renombrar_columnas": {
            "Fecha": "FECHA",
            "Docto. Nro.": "N_DOCUMENTO",
            "Detalle Movimiento": "DESCRIPCION",
            "Cheque o Cargo": "CHEQUES_CARGOS",
            "Deposito o Abono": "DEPOSITOS_ABONOS",
        },
        "columnas_salida": [
            "INDEX",
            "FECHA",
            "DESCRIPCION",
            "N_DOCUMENTO",
            "CHEQUES_CARGOS",
            "DEPOSITOS_ABONOS",
        ],
        "columnas_numericas": [
            "Cheque o Cargo",
            "Deposito o Abono",
        ],
    },
    "Banco Scotiabank": {
        "renombrar_columnas": {
            "Fecha": "FECHA",
            "Numero Documento": "N_DOCUMENTO",
            "Descripción": "DESCRIPCION",
            "Cargo": "CHEQUES_CARGOS",
            "Abono": "DEPOSITOS_ABONOS",
        },
        "columnas_salida": [
            "INDEX",
            "FECHA",
            "DESCRIPCION",
            "N_DOCUMENTO",
            "CHEQUES_CARGOS",
            "DEPOSITOS_ABONOS",
        ],
        "columnas_numericas": [
            "Cargo",
            "Abono",
        ],
    },
}
