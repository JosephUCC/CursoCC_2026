"""Microreto: el portero del café."""

energia = int(input('Cuanta energia tiene de 0-100?: '))

trae_cafe = input("¿Traes café? (si/no): ").lower().strip() == 'si'
if energia >= 30 or trae_cafe:
    mensaje = 'Bienvenido, pase adelante!'
elif energia < 30 and trae_cafe == False:
    mensaje = 'Lo sentimos, no puede pasar'
else:
    mensaje: 'El guarda esta confundido, revise las respuestas'

print(mensaje)
# TODO: usa and para detectar energía baja sin café.
# TODO: usa or para permitir energía suficiente o café.
# TODO: escribe mensajes claros para cada resultado.


