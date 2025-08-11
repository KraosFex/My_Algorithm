import math

# clases y Objetos.
# las clases son modelos que nos permiten contruir objetos.
# POO intenta abstraer lo mas importante de un objeto:

# Reglas Para construir una clase
    # Para toda clase en python debe existir un constructor __init__
    # Todo metodo de clase simpre, sin excepcion, recive como primer parametro self
    # Self es una referencial al objeto actual

# Ejemplo:
class Fraccion:
    num = 0
    den = 1

    def __init__ (self, num = 0, den = 1):
        self.num = num
        self.den = den

    def multiplica (self, b):
        num = self.num * b.num
        den = self.den * b.den
        r = Fraccion(num, den)
        return r

    def imprime(self):
        print(self.num, '/', self.den)

def main():
    a = Fraccion(7, 8)
    a.imprime()

class Galleta:
    def __init__(self) -> None:
        self.chocolate = False
        print("Acabas de crear un galleta.")


    def saborizador(self):
        if self.chocolate == False:
            self.chocolate = True
            self.sabor_de_galleta()
        else:
            self.chocolate = False
            self.sabor_de_galleta()


    def sabor_de_galleta(self):
        if self.chocolate == True:
            print("La galleta es de chocolate")
        else:
            print("La galleta no tiene sabor")

class Cart:
    def __init__(self, marca = None, modelo = None, año_de_procuccion = None) -> None:
        try:
            self.marca = marca
            self.modelo = modelo
            self.año_de_procuccion =  año_de_procuccion
            self.__numero_de_vehiculos_producido = 0
            self.__vehiculos_producidos = []
            if marca is None or modelo is None or año_de_procuccion is None:
                raise ValueError("Argumentos insuficientes, los argumentos deben estar completos.")
            print(f"Se ha registrado exitosamente un vehiculo de la marca {marca}, modelo {modelo}, año {año_de_procuccion}")
        except Exception as e:
            print(f"Error: {e}\nLos argumentos son:\n\tmarca del vehiculo, modelo del vehiculo y año de creacion del vehiculo")


    def __serializador_vehiculos(self, serie,  cantida):
        for n in range(cantida):
            numero_de_serie = serie + str(math.floor(math.e * len(self.__vehiculos_producidos)))
            self.__vehiculos_producidos.append({len(self.__vehiculos_producidos) : numero_de_serie})


    def total_de_vehiculos_producidos(self):
        print(f"se han fabricado un total {self.__numero_de_vehiculos_producido}, marca {self.marca}, modelo {self.modelo}, año {self.año_de_procuccion}")


    def fabricar(self, serie, cantidad):
        if cantidad <= 56:
            producion = cantidad
        elif cantidad > 56:
            producion = math.floor(cantidad - (cantidad * 0.16))

        self.__serializador_vehiculos(serie ,producion)
        self.__numero_de_vehiculos_producido += producion
        self.total_de_vehiculos_producidos()


    def ver_todos_los_vehiculos(self):
        for vehiculo in self.__vehiculos_producidos:
            print(vehiculo)
