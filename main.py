import pandas as pd
import glob
import matplotlib.pyplot as plt

# busco los archivos en la carpeta datos/
archivos_csv = glob.glob("datos/*.csv")
archivos_xlsx = glob.glob("datos/*.xlsx")

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

# guardo el consolidado limpio
df_limpio.to_excel("resultados/consolidado_limpio.xlsx", index=False)

# 6a. ventas por categoria (grafico de barras)
ventas_por_categoria = df_limpio.groupby('categoria')['precio_unitario'].sum()
ventas_por_categoria.plot(kind='bar', title='Ventas por Categoria')
plt.ticklabel_format(style='plain', axis='y')
plt.ylabel('Ventas totales ($)')
plt.xlabel('Categoria')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("resultados/grafico_categoria.png")
plt.show()

# 6b. participacion por vendedor (grafico de torta)
ventas_por_vendedor = df_limpio.groupby('vendedor')['precio_unitario'].sum()
ventas_por_vendedor.plot(kind='pie', autopct='%1.1f%%', title='Participacion de Ventas por Vendedor')
plt.ylabel('')
plt.tight_layout()
plt.savefig("resultados/grafico_vendedor.png")
plt.show()

# 6c. producto que mas se repite en las ventas
producto_mas_vendido = df_limpio['producto'].value_counts()
print(producto_mas_vendido)
print(f"Producto mas vendido: {producto_mas_vendido.index[0]} con {producto_mas_vendido.iloc[0]} ventas")