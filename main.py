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

    with open("resultados/log_automatizacion.txt", "a", encoding="utf-8") as f:
        f.write(f"Proceso ejecutado: {pd.Timestamp.now()}\n")
        f.write(f"Total de registros procesados: {len(df_limpio)}\n")
        f.write("---\n")

    # ============================================
    # Banner visual con resumen en pantalla
    # ============================================
    total_ventas = df_limpio['precio_unitario'].sum()
    print("=" * 40)
    print("  NUEVO REPORTE PROCESADO EXITOSAMENTE")
    print(f"  Total ventas acumuladas: ${total_ventas:,.0f}")
    print("=" * 40)

    # ============================================
    # Resumen ejecutivo en archivo de texto
    # (usamos df_limpio, no df_consolidado, para que
    # el resumen refleje los datos ya sin nulos ni duplicados)
    # ============================================
    categoria_top = df_limpio.groupby('categoria')['precio_unitario'].sum().idxmax()
    vendedor_top = df_limpio.groupby('vendedor')['precio_unitario'].sum().idxmax()

    # Métrica nueva 1: producto más vendido (reutilizando value_counts() de arriba)
    producto_top = producto_mas_vendido.index[0]
    unidades_producto_top = producto_mas_vendido.iloc[0]

    # Métrica nueva 2: promedio de venta por transacción
    promedio_venta = df_limpio['precio_unitario'].mean()

    with open("resultados/resumen_ejecutivo.txt", "w", encoding="utf-8") as f:
        f.write("RESUMEN EJECUTIVO - Bot de Ventas\n")
        f.write(f"Fecha: {pd.Timestamp.now()}\n\n")
        f.write(f"Categoria con mejor desempeño: {categoria_top}\n")
        f.write(f"Vendedor con mas ventas: {vendedor_top}\n")
        f.write(f"Producto mas vendido: {producto_top} ({unidades_producto_top} ventas)\n")
        f.write(f"Promedio de venta por transaccion: ${promedio_venta:,.0f}\n")
        f.write(f"Total de ventas acumuladas: ${total_ventas:,.0f}\n")


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