import math

class NegativeNumber(Exception):
    "Excepcion de tipo número negativo"
    pass

def raiz_cuadrada_num(number):
    if number < 0:
        raise NegativeNumber("Número negativo")
    return math.sqrt(number)

