"""Semana 8: la red hospitalaria nos contrata como analistas de datos.

Construimos el informe debajo de este inicio con GUIA_ESTUDIANTE.md.
Leemos la fuente preparada en fuente.py y contamos las menciones recibidas.
"""

from fuente import cargar_datos


USAR_RESPALDO = False  # Lo cambiamos solo si recibimos copias actualizadas.
registros, equivalencias, origen = cargar_datos(USAR_RESPALDO)
print("Fuente:", origen)
print("Registros recibidos:", len(registros))
print("Equivalencias publicadas:", len(equivalencias))

# Comencemos aquí con la muestra y después construyamos nuestro contador.
conteo_medicamento = {}
conteo_recetas = 0

for indice in range(len(registros)):
    registro = registros[indice]
    print(f'Paciente: {registro["paciente_cedula"]}')
    print(f'Nombre: {registro["paciente_nombre"]}')
    print(f'diagnostico: {registro["diagnostico"]}')
    print(f'medicamento: {registro["medicamentos"]}')

    for medicamento in registro['medicamentos']:
        if medicamento in conteo_medicamento:
            conteo_medicamento[medicamento] += 1
        else:
            conteo_medicamento[medicamento] = 1
        conteo_recetas += 1

    

print("Conteo de medicamentos:", conteo_medicamento)
print("Total de recetas:", conteo_recetas)
print("--------------------------------------------------")

conteo_medicamento = {}
conteo_recetas = 0
#fase 2 limpieza de datos
equivalencias = {
    "acetaminofén": "acetaminofen",
    "paracetamol": "acetaminofen",
    "antiácido": "antiacido",
    "losartán": "losartan"
}
conteo_hospital_paciente = {}

conteo_diagnosticos = {}

conteo_enfermedad = {}

for registro in registros:
    for medicamento in registro['medicamentos']:
        nombre = medicamento.strip().lower()
        #aplicacion fase 2
        if nombre in equivalencias:
            nombre = equivalencias[nombre]
        if nombre in conteo_medicamento:
            conteo_medicamento[nombre] += 1
        else:
            conteo_medicamento[nombre] = 1
        conteo_recetas += 1

    #cuantos pacientes por hospital
    hospital = registro['hospital']
    if hospital in conteo_hospital_paciente:
        conteo_hospital_paciente[hospital] += 1
    else:
        conteo_hospital_paciente[hospital] = 1

    #diagnostico registrados
    diagnostico = registro['diagnostico']
    if diagnostico in conteo_diagnosticos:
        conteo_diagnosticos[diagnostico] += 1
    else:
        conteo_diagnosticos[diagnostico] = 1

    #cantidad de pacietes por enfermedad
    enfermedad = registro['diagnostico']
    if enfermedad in conteo_enfermedad:
        conteo_enfermedad[enfermedad] += 1
    else:
        conteo_enfermedad[enfermedad] = 1


print("Conteo de medicamentos:", conteo_medicamento)
print("Total de recetas:", conteo_recetas)
print("Pacientes por hospital:", conteo_hospital_paciente)

for medicamento, cantidad in conteo_medicamento.items():
    print(f'Medicamento: {medicamento}, Cantidad: {cantidad}')
print("--------------------------------------------------")
for hospital, cantidad in conteo_hospital_paciente.items():
    print(f'Hospital: {hospital}, Cantidad de pacientes: {cantidad}')
print("--------------------------------------------------")
for diagnostico, cantidad in conteo_diagnosticos.items():
    print(f'Diagnóstico: {diagnostico}, Cantidad: {cantidad}')
print("--------------------------------------------------")
for enfermedad, cantidad in conteo_enfermedad.items():
    print(f'Enfermedad: {enfermedad}, Cantidad: {cantidad}')
print("--------------------------------------------------")
