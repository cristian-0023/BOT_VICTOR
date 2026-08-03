import pandas as pd
import glob

# -------------------------------------------------------------
# 1. BUSCAR Y LEER ARCHIVOS (CSV y XLSX)
# -------------------------------------------------------------
# Buscamos todos los archivos CSV y Excel en la carpeta actual
archivos_csv = glob.glob("*.csv")
archivos_xlsx = glob.glob("*.xlsx")

print(f"Archivos CSV encontrados: {archivos_csv}")
print(f"Archivos XLSX encontrados: {archivos_xlsx}")

# 2. GUARDAR DATAFRAMES EN UNA LISTA
lista_dataframe = []

# Lectura iterativa de archivos CSV
for archivo in archivos_csv:
    df = pd.read_csv(archivo)
    lista_dataframe.append(df)
    print(f"Leído: {archivo} - {len(df)} filas")

# Lectura iterativa de archivos XLSX
for archivo in archivos_xlsx:
    df = pd.read_excel(archivo)
    lista_dataframe.append(df)
    print(f"Leído: {archivo} - {len(df)} filas")


# -------------------------------------------------------------
# 3. HOMOGENEIZACIÓN DE COLUMNAS (Código adaptado de template.py)
# -------------------------------------------------------------
# Reto: Uno de los 4 archivos (sucursal_bogota.xlsx) tiene columnas con nombres distintos.
# 1. Identificar cuál archivo es: sucursal_bogota.xlsx
# 2. Identificar cuál columna única sirve para reconocerlo: 'Fecha_Venta'
# 3. Crear el diccionario de renombrado completo a las 7 columnas estándar

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


# -------------------------------------------------------------
# 4. CONSOLIDACIÓN Y LIMPIEZA DE DATOS
# -------------------------------------------------------------
# Consolidar la lista de DataFrames en un solo DataFrame unificado
df_consolidado = pd.concat(lista_dataframe, ignore_index=True)

# Limpieza 1: Eliminar filas vacías o con datos nulos (NaN)
df_limpio = df_consolidado.dropna()

# Limpieza 2: Eliminar filas totalmente duplicadas
df_limpio = df_limpio.drop_duplicates()

# Limpieza 3: Quitar espacios vacíos / sobrantes en las columnas de texto
for col in df_limpio.select_dtypes(include=['object', 'string']).columns:
    df_limpio[col] = df_limpio[col].astype(str).str.strip()

# -------------------------------------------------------------
# 5. RESULTADO FINAL
# -------------------------------------------------------------
print("\n=======================================================")
print("  REPORTE CONSOLIDADO Y LIMPIO")
print("=======================================================")
print(f"Total de columnas: {len(df_limpio.columns)} (Esperado: 7)")
print(f"Nombres de columnas: {list(df_limpio.columns)}")
print(f"Total de filas limpias sin duplicados ni vacíos: {len(df_limpio)}")
print("=======================================================")
print(df_limpio.head(10))