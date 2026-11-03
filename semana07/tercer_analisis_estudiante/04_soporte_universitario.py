"""Caso 4: analice los registros de soporte sin crear funciones propias."""

from incidencias import incidencias

# Cada incidencia es un diccionario: id, provincia, categoria,
# minutos_atencion y resuelto (True o False).

# TODO: Prepare un acumulador de minutos, un diccionario para contar
#       "Acceso", "Equipo" y "Red", un contador de casos pendientes,
#       un set de provincias con pendientes, una lista de tuplas de casos
#       urgentes y una tupla para el caso con más minutos de atención.
minutos_total = 0
conteo_categoria = {
    "Acceso": 0, 
    "Equipo": 0, 
    "Red": 0
    }
pendientes = 0
provincias_pendientes = set()
casos_urgentes = []
caso_mas_largo = ("", 0)  # (id, minutos)
# TODO: Recorra incidencias una sola vez. Actualice los acumuladores y el
#       conteo de la categoría de cada registro.
for incidencia in incidencias:
    minutos_total += incidencia['minutos_atencion']
    categoria = incidencia['categoria']
    identificador = incidencia['id']
    conteo_categoria[categoria] += 1
    
# TODO: Si un caso NO está resuelto, cuéntelo y agregue su provincia al set.
#       Si, además, tiene 60 minutos o más, agregue (id, minutos) a la lista
#       de casos urgentes. Actualice la tupla del caso más largo si corresponde.
    if incidencia['resuelto']== False:
        pendientes += 1
        provincias_pendientes.add(incidencia['provincia'])
        if incidencia['minutos_atencion'] >= 60:
            casos_urgentes.append((incidencia['id'], incidencia['minutos_atencion']))
    # Actualizar el caso más largo si corresponde
    if incidencia['minutos_atencion'] > caso_mas_largo[1]:
        caso_mas_largo = (incidencia['id'], incidencia['minutos_atencion'])
# TODO: Muestre total y promedio de minutos, conteo por categoría, cantidad
#       de pendientes, provincias con pendientes, casos urgentes y caso más
#       largo. Compruebe también si "San Jose" pertenece al set.
print("Total de minutos: ", minutos_total)
print("Promedio de minutos: ", minutos_total / len(incidencias))
print("Conteo por categoría: ", conteo_categoria)
print("Cantidad de casos pendientes: ", pendientes)
print("Provincias con casos pendientes :", provincias_pendientes)
print("Casos urgentes:", casos_urgentes)
print("Caso con más minutos de atención: ", caso_mas_largo)
print("San Jose tiene casos pendientes?", "San Jose" in provincias_pendientes)
# Control: 10 casos; 500 minutos; promedio 50; Acceso 4, Equipo 3, Red 3;
# 4 pendientes en 4 provincias; urgentes INC-02, INC-05 e INC-07;
# más largo INC-07 con 95 minutos; hay pendientes en San Jose.
# Prueba: cambie temporalmente INC-07 a resuelto=True. Debe salir de la
# lista de urgentes, del conteo de pendientes y del set de provincias
# pendientes, pero seguir como caso más largo. Restaure incidencias.py.
