"""Diez sedes ficticias EmprendeCR para analizar en un archivo nuevo.

Las primeras seis proceden del caso anterior; las últimas cuatro amplían el
escenario de práctica. Mantenga los registros sin cambios durante la actividad.
"""

sedes = [
    {
        "nombre": "Soda San Pedro",
        "provincia": "San Jose",
        "tipo": "Alimentacion",
        "ventas": [85000, 92000, 78000, 110000, 97000],
        "meta": 450000,
    },
    {
        "nombre": "Panaderia Cartago",
        "provincia": "Cartago",
        "tipo": "Panaderia",
        "ventas": [65000, 70000, 72000, 69000, 75000],
        "meta": 380000,
    },
    {
        "nombre": "Cafeteria Liberia",
        "provincia": "Guanacaste",
        "tipo": "Cafeteria",
        "ventas": [98000, 105000, 99000, 120000, 115000],
        "meta": 500000,
    },
    {
        "nombre": "Feria de Heredia",
        "provincia": "Heredia",
        "tipo": "Feria",
        "ventas": [72000, 76000, 80000, 78000, 74000],
        "meta": 390000,
    },
    {
        "nombre": "Marisqueria Puntarenas",
        "provincia": "Puntarenas",
        "tipo": "Restaurante",
        "ventas": [115000, 108000, 112000, 118000, 121000],
        "meta": 560000,
    },
    {
        "nombre": "Tienda Escazu Local",
        "provincia": "San Jose",
        "tipo": "Comercio",
        "ventas": [88000, 91000, 87000, 94000, 90000],
        "meta": 460000,
    },
    {
        "nombre": "Libreria Alajuela",
        "provincia": "Alajuela",
        "tipo": "Comercio",
        "ventas": [90000, 95000, 100000, 85000, 105000],
        "meta": 480000,
    },
    {
        "nombre": "Tienda Limon Centro",
        "provincia": "Limon",
        "tipo": "Comercio",
        "ventas": [70000, 80000, 75000, 85000, 90000],
        "meta": 390000,
    },
    {
        "nombre": "Ferreteria Desamparados",
        "provincia": "San Jose",
        "tipo": "Ferreteria",
        "ventas": [50000, 60000, 55000, 65000, 70000],
        "meta": 400000,
    },
    {
        "nombre": "Vivero Paraiso",
        "provincia": "Cartago",
        "tipo": "Vivero",
        "ventas": [65000, 70000, 60000, 75000, 80000],
        "meta": 350000,
    },
]
mayor_venta = 0
menor_venta = float("inf") 
sede_mayor_venta = ""
sede_menor_venta = ""
mensaje_cumplimiento = ""

for sede in sedes:
    nombre = sede["nombre"]
    ventas = sede["ventas"]
    meta = sede["meta"]
    total_ventas = sum(ventas)

    if total_ventas > mayor_venta:
        mayor_venta = total_ventas
        sede_mayor_venta = nombre

    if total_ventas < menor_venta:
        menor_venta = total_ventas
        sede_menor_venta = nombre

    
    promedio_ventas = total_ventas / len(ventas)

    if total_ventas > meta:
        mensaje_cumplimiento = f"{nombre} ha superado la meta de ventas."
    elif total_ventas == meta:
        mensaje_cumplimiento = f"{nombre} ha alcanzado la meta de ventas."
    else:
        mensaje_cumplimiento = f"{nombre} no ha alcanzado la meta de ventas."
    
    print(f"Sede: {nombre}")
    print(f"Total de ventas: {total_ventas}")
    print(f"Promedio de ventas: {promedio_ventas}")
    print(f"Meta de ventas: {meta}")
    print(mensaje_cumplimiento)
    print("-" * 40)

print(f"La sede con mayor venta es: {sede_mayor_venta} con un total de {mayor_venta}")
print(f"La sede con menor venta es: {sede_menor_venta} con un total de {menor_venta}")

