import math

def area_rectangulo(base, altura):
    resultado = base * altura
    return resultado


def area_circulo(radio):
    resultado = math.pow(radio, 2) * math.pi
    return resultado


print(area_rectangulo(15, 10))
print(area_circulo(5))
