#soluciob mision kit seguro
#autor: joseph gamboa fecha:2026/10/06

nombre = input('Nombre: ').strip().upper()
kit = input('Tipo de kit: ').strip().lower()
autorizacion = input('Tiene autorizacion (si/no)?: ').strip().lower() == 'si'

try:
    cantidad = int(input('digite la cantidad de kits: '))
except ValueError:
    print('Error cantidad invalida, asignada -1')
    cantidad = -1

try:
    dias = int(input('Dias de prestamo (1-100): '))
except ValueError:
    print('Error cantidad dias invalida. asignada -1')
    dias = -1
    
resultado = ''
if nombre == '' or not kit or cantidad < 1 or dias < 1:
    resultado = 'Registro rechazado: datos invalidos'
elif autorizacion and cantidad <= 3 and dias <= 7:
    resultado = f'solicitud aprovada para {nombre}: {cantidad} kit(s) de {kit}'
elif cantidad > 3 or dias > 7:
    resultado = 'solicitud enviada a revision'
else:
    resultado = 'solicitud rechazada: se requiere autorizacion'
    
print(resultado)