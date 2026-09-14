# Reflexión — Sistema de Automatización

**¿Qué hace "os.listdir(ruta_datos)"?**
Básicamente me lista todo lo que hay dentro de la carpeta datos, o sea los nombres de los archivos. Lo uso para poder revisar qué archivos hay ahí y compararlos con los que ya procesé antes, así el script sabe si llegó algo nuevo.

**¿Qué diferencia hay entre "set" y "lista" para guardar archivos vistos?**
La lista puede repetir cosas y para buscar si un archivo ya está ahí tiene que revisar uno por uno, entonces si hay muchos archivos se vuelve más lento. El set no deja que se repitan los datos y buscar si algo ya existe es casi instantáneo. Por eso para guardar los archivos que ya vi me convenía más usar un set, no necesito que estén en orden ni que se repitan, solo saber rápido si ya lo procesé o no.

**¿Qué hace drop_duplicates() y por qué es importante aquí?**
Elimina las filas que están repetidas en el DataFrame. Aquí es importante porque estoy juntando reportes de varias sucursales y si por alguna razón un archivo se llega a procesar dos veces, sin esto las ventas quedarían duplicadas y el consolidado final mostraría números que no son reales.

**¿Cuántos commits tiene tu repo? Menciona 2 de tus mensajes**
Mi repo tiene 13 commits. Dos de mis mensajes fueron:
- "agregar sistema de automatización"
- "Solucion a columnas distintas, consolidacion de 7 columnas y limpieza de datos"

**¿Qué mejora le harías a este sistema?**
Le agregaría un manejo de errores mejor, porque si llega un archivo dañado o con columnas que no cuadran el script se puede caer. También me gustaría que en vez de guardar los "archivos vistos" solo en memoria, quedaran guardados en un archivo para que si se reinicia el script no se pierda ese registro.

**¿Qué fue lo que más te gustó aprender?**
Lo que más me gustó fue ver cómo un script puede estar "vigilando" una carpeta y reaccionar solo cuando llega algo nuevo, sin que yo tenga que estar corriendo todo manualmente. Fue interesante juntar lo de manejo de archivos con pandas y verlo funcionar de principio a fin.