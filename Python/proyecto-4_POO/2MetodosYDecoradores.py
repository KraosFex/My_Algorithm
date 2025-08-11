import math

# Tengo que agregar @classmethod y @staticmetod

class Carro:
    def __init__(self, marca, modelo, año) -> None:
        try:
            self.marca = marca
            self.modelo = modelo
            self.año_de_procuccion =  año
            self.__numero_de_vehiculos_producido = 0
            self.__vehiculos_producidos = []
            if marca is None or modelo is None or año is None:
                raise ValueError("Argumentos insuficientes, los argumentos deben estar completos.")
            print(f"Se ha registrado exitosamente un vehiculo de la marca {marca}, modelo {modelo}, año {año}")
        except Exception as e:
            print(f"Error: {e}\nLos argumentos son:\n\tmarca del vehiculo, modelo del vehiculo y año de produccion.")

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
