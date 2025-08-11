# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 21:29:45 2023

@author: KraosFex
"""

class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
        
    def __str__(self):
        cad = "Color del vehiculo {}, {} ruedas del vehiculo"
        return cad.format(self.color, self.ruedas)
    

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def __str__(self):
        cad = ", {} Km/h, {} cc"
        return super().__str__() + cad.format(self.velocidad, self.cilindrada)
    

toyota = Coche("rojo", 4, 100, 78000)

print(toyota)
