import time
import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

RUTA_DATOS = "datos/"


def procesar_todo():
    archivos_csv = glob.glob("datos/*.csv")
    archivos_xlsx = glob.glob("datos/*.xlsx")

    print(f"Archivos CSV encontrados: {archivos_csv}")
    print(f"Archivos XLSX encontrados: {archivos_xlsx}")

    lista_dataframe = []

    for archivo in archivos_csv:
        df = pd.read_csv(archivo)
        lista_dataframe.append(df)
        print(f"Leído: {archivo} - {len(df)} filas")

    for archivo in archivos_xlsx:
        df = pd.read_excel(archivo)
        lista_dataframe.append(df)
        print(f"Leído: {archivo} - {len(df)} filas")

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

    df_consolidado = pd.concat(lista_dataframe, ignore_index=True)

    df_limpio = df_consolidado.dropna()
    df_limpio = df_limpio.drop_duplicates()

    for col in df_limpio.select_dtypes(include=['object', 'string']).columns:
        df_limpio[col] = df_limpio[col].astype(str).str.strip()

    print("columnas finales:", list(df_limpio.columns))
    print("total filas:", len(df_limpio))
    print(df_limpio.head(10))

    df_limpio.to_excel("resultados/consolidado_limpio.xlsx", index=False)

    ventas_por_categoria = df_limpio.groupby('categoria')['precio_unitario'].sum()
    ventas_por_categoria.plot(kind='bar', title='Ventas por Categoria')
    plt.ticklabel_format(style='plain', axis='y')
    plt.ylabel('Ventas totales ($)')
    plt.xlabel('Categoria')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig("resultados/grafico_categoria.png")
    plt.close()

    ventas_por_vendedor = df_limpio.groupby('vendedor')['precio_unitario'].sum()
    ventas_por_vendedor.plot(kind='pie', autopct='%1.1f%%', title='Participacion de Ventas por Vendedor')
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig("resultados/grafico_vendedor.png")
    plt.close()

    producto_mas_vendido = df_limpio['producto'].value_counts()
    print(producto_mas_vendido)
    print(f"Producto mas vendido: {producto_mas_vendido.index[0]} con {producto_mas_vendido.iloc[0]} ventas")

    with open("resultados/log_automatizacion.txt", "a") as f:
        f.write(f"Proceso ejecutado: {pd.Timestamp.now()}\n")
        f.write(f"Total de registros procesados: {len(df_limpio)}\n")
        f.write("---\n")


os.makedirs("resultados", exist_ok=True)

print("Procesando estado inicial de datos/...")
procesar_todo()

archivos_vistos = set(os.listdir(RUTA_DATOS))
print("Monitoreando carpeta datos/... (Ctrl+C para detener)")

while True:
    archivos_actuales = set(os.listdir(RUTA_DATOS))
    archivos_nuevos = archivos_actuales - archivos_vistos

    nuevos_relevantes = {
        a for a in archivos_nuevos if a.endswith((".csv", ".xlsx"))
    }

    if nuevos_relevantes:
        print(f"Nuevo archivo detectado: {nuevos_relevantes}")
        procesar_todo()

    archivos_vistos = archivos_actuales
    time.sleep(5)