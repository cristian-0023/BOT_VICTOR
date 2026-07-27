import pandas as pd
import glob as glob

#1.Buscar datos y leer archivos

df_medellin = pd.read_csv("sucursal_medellin.csv")
#print(df_medellin)

df_bogota = pd.read_excel("sucursal_bogota.xlsx")
#print(df_bogota.head(3))

#print(df_bogota.columns)
#print(df_medellin.columns)


archivos_csv = glob.glob("*.csv")
print(f"Archivs_csv {archivos_csv}")

archivos_xlsx = glob.glob("*.xlsx")
print(f"Archivs_xlsx {archivos_xlsx}")


#2.Guardar en una lista

lista_dataframe = []

for archivo in archivos_csv:
    df = pd.read_csv(archivo)
    lista_dataframe.append(df)
    print(f"leido: {archivo} - {len(df)} filas")
    
    
for archivo in archivos_xlsx:
    df = pd.read_excel(archivo)
    lista_dataframe.append(df)
    print(f"leido: {archivo} - {len(df)} filas")