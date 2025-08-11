#!/usr/bin/env python3

class Animal:
  VITALIDAD = 1

  def __init__(self, salud = 1, hambre = 1, decendencia = 0, edad = 0) -> None:
    self.salud = salud
    self.hambre = hambre
    self.decendencia = decendencia
    self.edad = edad

  @property
  def vivo(self):
    estado = self.salud / self.VITALIDAD
    if estado <= 0:
      return False
    else:
      return True

  def __str__(self) -> str:
    if self.vivo == True:
      return f"El animal esta vivo:\nEdad:{self.edad}\nSalud:{self.salud}\nHambre:{self.hambre}\nDecendencia:{self.decendencia}"
    else:
      return "El animal esta muerto"

class Lagartijo(Animal):
  def __init__(self, subEspecie=None):
    super().__init__(salud=10, hambre=5)
    self.especie = "Lagartijo"
    self.subEspecie = subEspecie


if __name__ == "__main__":
  LagartijoA = Lagartijo()

  print(LagartijoA)
