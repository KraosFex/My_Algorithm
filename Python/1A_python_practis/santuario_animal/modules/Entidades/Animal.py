#!/usr/bin/env python3

class Animal:
  def __init__(self, especie:str, nombre_animal:str, edad:int=0, tamano:int=1, peso:int=500) -> None:
    self.especie = especie
    self.nombre = nombre_animal
    self.edad = edad
    self.tamano = f"{tamano}cm"
    self.peso = f"{peso}g"

  def __str__(self):
    return f"{self.nombre} es un {self.especie}, tiene {self.edad} años y mide {self.tamano}"
