import pandas as pd 

#Ruta del archivo exel.
path = "./ofertas_de_empleo.xlsx"

openFile = pd.read_excel(path, engine="openpyxl", sheet_name="Hoja1")

data = openFile.values 

for i in data:
    print(i)