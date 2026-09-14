# Reflexión — Sistema de Automatización BOT_VICTOR

## ¿Qué hace "os.listdir(ruta_datos)"?
Devuelve una lista con los nombres de todos los archivos y carpetas que hay dentro de `ruta_datos`. En este proyecto se usa para revisar la carpeta `datos/` y detectar qué archivos `sucursal_*.csv/xlsx` existen en cada ejecución, para luego compararlos contra los que ya se procesaron.

## ¿Qué diferencia hay entre "set" y "lista" para guardar archivos vistos?
- Una **lista** permite duplicados y buscar en ella recorre elemento por elemento (O(n)), lo que la hace más lenta si hay muchos archivos.
- Un **set** no permite duplicados y verificar si un archivo ya existe es prácticamente instantáneo (O(1)) porque usa hashing internamente.

Para "archivos vistos" conviene un `set`: no importa el orden, no queremos duplicados, y la comprobación `archivo in vistos` es mucho más eficiente.

## ¿Qué hace drop_duplicates() y por qué es importante aquí?
Elimina filas repetidas de un DataFrame de pandas. Es importante porque el sistema consolida datos de 4 sucursales en cada corrida, y si un mismo reporte se procesa más de una vez (por ejemplo, si el archivo se vuelve a detectar), sin `drop_duplicates()` las ventas quedarían duplicadas y el consolidado final (y los gráficos) mostrarían cifras infladas.

## ¿Cuántos commits tiene tu repo? Menciona 2 de tus mensajes
[Reemplaza con el número real de tu repo — revisa con `git log --oneline | wc -l`]

Dos mensajes de commit:
- "agregar sistema de automatización"
- "actualizar README con automatización"

## ¿Qué mejora le harías a este sistema?
[Ejemplos que puedes adaptar a tu criterio real: agregar manejo de errores más robusto si un archivo llega corrupto o con columnas faltantes; enviar una notificación (correo o Slack) cuando se detecte un archivo nuevo; guardar el registro de "archivos vistos" en un archivo persistente (JSON) en vez de en memoria, para que sobreviva si el script se reinicia; agregar pruebas unitarias.]

## ¿Qué fue lo que más te gustó aprender?
[Respuesta personal — por ejemplo: ver cómo un script puede vigilar una carpeta en tiempo real y reaccionar automáticamente, conectando conceptos de manejo de archivos, pandas y automatización en un flujo completo.]