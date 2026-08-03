import pandas as pd
import glob

# busco los archivos en la carpeta, no se cuantos hay de cada tipo
archivos_csv = glob.glob("*.csv")
archivos_xlsx = glob.glob("*.xlsx")

print(f"Archivos CSV encontrados: {archivos_csv}")
print(f"Archivos XLSX encontrados: {archivos_xlsx}")

lista_dataframe = []

# leo todos los csv primero
for archivo in archivos_csv:
    df = pd.read_csv(archivo)
    lista_dataframe.append(df)
    print(f"Leído: {archivo} - {len(df)} filas")

# despues los xlsx
for archivo in archivos_xlsx:
    df = pd.read_excel(archivo)
    lista_dataframe.append(df)
    print(f"Leído: {archivo} - {len(df)} filas")

# el archivo raro trae la columna Fecha_Venta, los otros 3 no
# entonces con eso lo identifico y renombro solo ese
for i, df in enumerate(lista_dataframe):
    if 'Fecha_Venta' in df.columns:
        lista_dataframe[i] = df.rename(columns={
            'Fecha_Venta': 'fecha',
            'Producto': 'producto',
            'Categoria': 'categoria',
            'Cant': 'cantidad',
            'Valor_Unitario': 'precio_unitario',
            'Vendedor': 'vendedor',
            'Pago': 'metodo_pago'
        })

# ahora si uno todo en un solo dataframe
df_consolidado = pd.concat(lista_dataframe, ignore_index=True)

# quito filas vacias y duplicadas
df_limpio = df_consolidado.dropna()
df_limpio = df_limpio.drop_duplicates()

# limpio espacios de mas en las columnas de texto
for col in df_limpio.select_dtypes(include=['object', 'string']).columns:
    df_limpio[col] = df_limpio[col].astype(str).str.strip()

# reviso que haya quedado bien: 7 columnas y sin basura
print("columnas finales:", list(df_limpio.columns))
print("total filas:", len(df_limpio))
print(df_limpio.head(10))