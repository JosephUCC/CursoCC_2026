"""Plantilla guiada: análisis de ventas de dos tiendas, sin ciclos."""

dias = ['Lunes', 'Martes','Miercoles','Jueves','Viernes']
ventas_centro = [125000, 98000, 147000, 132000, 110000]
ventas_norte = [140000, 135000, 150000, 145000, 155000]
meta_centro = 640000
meta_norte = 700000

# TODO: calcula total, cantidad, mayor y menor para Centro.
total_centro = sum(ventas_centro)#suma todas las variables
cantidad_centro = len(ventas_centro)#cuenta la cantidad de indices en el arreglo
maximo_centro = max(ventas_centro)#venta maxima
minimo_centro = min(ventas_centro)#venta minima
#sacamos el dia que mas se vendio y el monto mismo
dia_mayor = dias[ventas_centro.index(maximo_centro)]
#imprimimos el dia y ese monto maximo
print(dia_mayor, maximo_centro)

# TODO: calcula promedio, rango, diferencia y porcentaje para Centro.
promedio_centro = total_centro / cantidad_centro#promedio ventas diarias
porcentaje_centro = total_centro * 100 / meta_centro#porcentaje de ventas

# TODO: repite los indicadores para Norte.
total_norte = sum(ventas_norte)
cantidad_norte = len(ventas_norte)
promedio_norte = total_norte / cantidad_norte
maximo_norte = max(ventas_norte)
minimo_norte = min(ventas_norte)
porcentaje_norte = total_norte * 100 / meta_norte


# TODO: decide si cada tienda superó, igualó o no alcanzó su meta.
if total_centro > meta_centro:
    estado_centro = 'Meta superada!'
elif total_centro == meta_centro:
    estado_centro = 'Meta alcanzada'
else:
    estado_centro = 'No se logro la meta'
    
if total_norte > meta_norte:
    estado_norte = 'Meta superada!'
elif total_norte == meta_norte:
    estado_norte = 'Meta alcanzada'
else:
    estado_norte = 'No se logro la meta'
# TODO: compara los totales y los rangos.
if total_centro > total_norte:
    venta_mayor_ventas = 'tienda de Centro'
elif total_norte > total_centro:
    venta_mayor_ventas = 'tienda del Norte'
else:
    venta_mayor_ventas = 'Ambas tiendas tienen el mismo total'
# TODO: presenta un reporte con etiquetas claras y f-strings.
print('--COMPARACION SEMANAL DE TIENDAS--')
print('-' * 70)
print('Tienda Central\n')
print(f"Centro | Total: ₡{total_centro:,.2f} | Meta ₡{meta_centro:,.2f} | Cumplimiento {porcentaje_centro:.0f}%")
print(f"Centro logro {estado_centro}")
print(f"Venta maxima: ₡{maximo_centro:,.2f} | Venta Minima: ₡{minimo_centro:,.2f}")

print('-' * 70)
print('Tienda del Norte\n')
print(f"Norte | Total: ₡{total_norte:,.2f} | Meta ₡{meta_norte:,.2f} | Cumplimiento {porcentaje_norte:.0f}%")
print(f"Centro logro {estado_norte}")
print(f"Venta maxima: ₡{maximo_norte:,.2f} | Venta Minima: ₡{minimo_norte:,.2f}")
print('-' * 70)
print(f'La mayor venta la tuvo: {venta_mayor_ventas}')
# TODO: escribe las tres conclusiones solicitadas en la guía.
