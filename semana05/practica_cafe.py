indice_producto = 0
producto = ['cafe',5000,20]
nombre = producto[0]
precioActual = producto[1]
unidadesActuales = producto[2]
descuento = precioActual * 15 / 100
precioPromocional = precioActual - descuento
ingreso_actual = precioActual * unidadesActuales
proyeccion = unidadesActuales * 20 / 100
unidadesProyectadas = unidadesActuales + proyeccion
ingresoProyectado = precioPromocional * unidadesProyectadas
diferencia = ingresoProyectado - ingreso_actual

print('ANALISIS DE PROMOCION')
print(f'Producto: {nombre}')
print(f'Precio actual: ₡{precioActual}')
print(f'Unidades actuales: {unidadesActuales}')
print(f'Ingreso actual: ₡{ingreso_actual}')
print(f'Descuento: {descuento}')
print(f'Precio promocional: ₡{precioPromocional}')
print(f'Unidades proyectadas (presupuesto + 20%): {unidadesProyectadas}')
print(f'Ingreso con promocion: ₡{ingresoProyectado}')
print(f'Diferencia: ₡{diferencia}')
if diferencia > 0:
    print('Lanzar')
else:
    print('No lanzar')