#!/urs/bin/env python3

from Animal import Animal

class Hombre(Animal):
  def __init__(self, nombre):
    super().__init__(salud=10, hambre=15)
    self.nombre = nombre
    self.lvl = 1

  def __str__(self):
    describir_obj = f"{self.nombre} es un {self.__class__.__name__}:"
    datos_instacia_hombre = f"Level:{self.lvl}\nEdad:{self.edad}\nSalud:{self.salud}\nHambre:{self.hambre}\nDecendencia:{self.decendencia}"
    return f'{describir_obj}\n{datos_instacia_hombre}'

Rafael = Hombre("Rafael")

print(Rafael)
