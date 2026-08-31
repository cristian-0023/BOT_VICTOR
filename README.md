# Bot de Ventas

Script en Python que consolida reportes de ventas de 4 sucursales (Medellín, Bogotá, Cali, Barranquilla) en distintos formatos (CSV/XLSX), limpia los datos y genera un análisis con gráficos.

## Resultados

- Categoría con más ventas: Electrónica (~$2.600.000) vs Ropa (~$1.600.000)
- Vendedora con más ventas: Camila Ruiz (33.7% de participación)
- Producto más vendido: Cargador USB-C (8 ventas)

## Cómo ejecutar

pip install pandas matplotlib openpyxl
python main.py

## Automatización

El script no se ejecuta una sola vez: al correr `python main.py`, primero procesa lo que ya haya en `datos/`, y después se queda vigilando esa carpeta de forma indefinida.

**Cómo detecta archivos nuevos:** cada 5 segundos compara la lista de archivos que hay en `datos/` contra la última lista que guardó en memoria. La diferencia entre ambas listas son los archivos nuevos. No usa ninguna librería externa de monitoreo, solo `os.listdir()` y una resta de conjuntos (`set`).

**Qué pasa cuando encuentra uno:** si el archivo nuevo termina en `.csv` o `.xlsx`, se dispara todo el proceso de nuevo: lee **todos** los archivos de `datos/` (no solo el nuevo), consolida, limpia duplicados y vacíos, normaliza la columna con nombres distintos (`Fecha_Venta`), regenera el consolidado y los dos gráficos, y agrega una línea al log en `resultados/log_automatizacion.txt` con la fecha y el total de registros procesados. Así el consolidado y los gráficos siempre reflejan el estado completo de la carpeta, no solo el último archivo que llegó.