"""Microreto independiente: sumar tiempos con una función y un acumulador."""


ESPERAS = [12, 20, 18]


def sumar_esperas(minutos):
    """Devuelve la suma de los minutos recibidos en horas."""
    total = 0

    for minuto in minutos:
        # TODO: acumule cada minuto en total.
        total += minuto
    total = total / 60
    return f'horas: {total:.2f}'


#TODO: llame a la función sumar_esperas y guarde el resultado en una variable. Luego, imprima el resultado en horas.
print(sumar_esperas(ESPERAS))
horas_extra = sumar_esperas([15, 25, 30, 10, 5, 20])
print(f'Horas extra: {horas_extra}')