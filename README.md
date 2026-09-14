## Análisis de negocio

**¿Qué categoría de productos deberíamos priorizar en inventario y promociones?**
Electrónica es la categoría con mejor desempeño en ventas totales, por encima de Ropa. Conviene asegurar stock de esa línea antes que la otra.

**¿Qué vendedor está generando más ingresos y qué se puede aprender de su desempeño?**
Carlos es el vendedor con más ventas acumuladas. Vale la pena revisar qué está haciendo distinto (turnos, sucursal, tipo de producto que mueve) para replicarlo con el resto del equipo.

**¿Cuál es el producto que más rota y qué implica para el abastecimiento?**
El Cargador USB-C es el producto más vendido con 8 unidades. Es un producto de bajo precio unitario y alta rotación, así que el riesgo de quiebre de stock es más urgente ahí que en productos de precio alto pero baja rotación.

**¿El promedio de venta por transacción es sano para el negocio?**
El promedio de venta por transacción es de $129,091. Sirve como línea base: si en próximos reportes ese promedio baja mientras el número de transacciones sube, puede indicar que se está vendiendo más volumen pero de productos más baratos (como el cargador), lo cual cambia la estrategia de precios o de combos.

## Conclusión

Con 57 transacciones consolidadas de 4 sucursales, el negocio depende fuertemente de Electrónica y de un producto de bajo costo (Cargador USB-C) para su volumen de ventas, mientras que el ingreso está concentrado en un vendedor top (Carlos). Esto sugiere dos riesgos a vigilar: dependencia de un solo producto de alta rotación y baja diversificación en el desempeño del equipo de ventas.

## Reflexión final

Como dueño del negocio, confiaría en este sistema para **monitorear tendencias y alertar** (qué categoría cae, qué vendedor se estanca, si el promedio de transacción baja), pero no para **tomar decisiones finales por sí solo**. Las razones:

- El script no distingue causas: si el promedio de venta baja, no sabe si es por una promoción intencional, un error de precios cargado mal, o una caída real de demanda. Esa distinción la tiene que hacer una persona.
- `dropna()` y `drop_duplicates()` eliminan filas automáticamente sin que nadie revise si eran errores de digitación o ventas reales mal registradas — eso puede estar ocultando pérdidas de datos importantes.
- Las métricas están calculadas sobre datos acumulados desde el inicio, sin filtro de fechas: no distingue "esta semana" de "todo el histórico", así que una mala racha reciente puede quedar diluida entre los buenos meses anteriores.

En resumen: lo usaría como el primer filtro que me dice **dónde mirar**, no como el que me dice **qué decidir**.