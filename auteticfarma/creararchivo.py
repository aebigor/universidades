import pandas as pd

# Definir los encabezados del DataFrame
encabezados = [
    "título de la oferta", "área", "cargo equivalente", "nivel educativo", "subnivel",
    "si se publica el nombre", "cantidad de vacantes", "rango del salario en millones",
    "si se publica el salario", "período de salario", "descripción", "requisitos",
    "ubicación de la oferta", "departamento", "ciudad", "industria de la empresa",
    "sector", "subsectores", "educación requerida", "tipo de candidato", 
    "años totales de experiencia", "experiencia requerida en el cargo", 
    "tipo de contrato", "tiempo dedicado"
]

# Crear un DataFrame vacío con esos encabezados
df = pd.DataFrame(columns=encabezados)

# Mostrar el DataFrame vacío
print(df)

# Definir el nombre del archivo Excel de salida
nombre_archivo_excel = "ofertas_de_empleo.xlsx"

# Guardar el DataFrame en un archivo Excel
df.to_excel(nombre_archivo_excel, index=False, engine='openpyxl')

print(f'Archivo Excel creado con éxito: {nombre_archivo_excel}')
