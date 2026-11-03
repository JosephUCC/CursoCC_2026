"""Caso 3: comparación de precios de un producto en cinco ferias."""

producto = "Tomate"
precios = [900, 850, 1000, 950, 1200]

# TODO: Calcule promedio, mínimo, máximo y rango (máximo - mínimo).
promedio = sum(precios) / len(precios)
maximo = max(precios)
minimo = min(precios)
rango = maximo - minimo
# TODO: Recorra precios con while y un índice para contar los que SUPERAN
#       el promedio. Aumente el índice en cada vuelta para terminar el ciclo.
indice = 0
superan_promedio = 0
while indice < len(precios):
    if precios[indice] > promedio:
        superan_promedio += 1
    indice += 1
# TODO: Clasifique el rango: >=300 variación alta; >=150 moderada; si no, baja.
if rango >= 300:
    clasificacion_rango = 'variacion alta'
elif rango >= 150:
    clasificacion_rango = 'variacion moderada'
else:
    clasificacion_rango = 'variacion baja'
# TODO: Muestre producto y todos los resultados.
print(f'Producto: {producto}')
print(f'Promedio: {promedio}')
print(f'Minimo: {minimo}')
print(f'Maximo: {maximo}')
print(f'Rango: {rango}')
print(f'Precios que superan el promedio: {superan_promedio}')
print(f'Clasificacion del rango: {clasificacion_rango}')
# Con los datos base: promedio ₡980, mínimo ₡850, máximo ₡1200,
# rango ₡350, 2 precios sobre el promedio, variación alta.
# Prueba de código: use temporalmente cinco precios iguales y compruebe que
# el rango sea cero y ninguno supere el promedio. Restaure la lista.
