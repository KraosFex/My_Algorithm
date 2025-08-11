# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 22:10:14 2023

@author: KraosFex
"""

class Fraccion():
    def __init__(self, numerador=0, denominador=1 ):
        if isinstance(numerador, int):
             self.numerador = numerador
        else:
            self.numerador = 0
        if isinstance(denominador, int) and denominador != 0 :
            self.denominador = denominador
        else:
            self.denominador = 1
        self.simplificaFracion()
        
    def __str__(self):
        cad = "{} / {}"
        return cad.format(self.numerador, self.denominador)
    
    def __mul__(self, obj):
        factor_numerador = self.numerador * obj.numerador
        factor_denominador = self.denominador * obj.denominador
        fraccion_factor_de_dos_fracciones = Fraccion(factor_numerador,factor_denominador)
        fraccion_factor_de_dos_fracciones.simplificaFracion()
        return fraccion_factor_de_dos_fracciones
    
    def __div__(self, obj):
      factor_numerador = self.numerador * obj.denominador
      factor_denominador = self.denominador * obj.numerador
      fraccion_factor_de_dos_fracciones = Fraccion(factor_numerador, factor_denominador)
      fraccion_factor_de_dos_fracciones.simplifica()
      return fraccion_factor_de_dos_fracciones

    def __add__(self, obj):
      factor_numerador = self.numerador * obj.denominador + self.denominador * obj.numerador 
      factor_denominador = self.denominador * obj.denominador
      fraccion_factor_de_dos_fracciones = Fraccion(factor_numerador, factor_denominador)
      fraccion_factor_de_dos_fracciones.simplifica()
      return fraccion_factor_de_dos_fracciones
    
    def __sub__(self, obj):
      factor_numerador = self.numerador * obj.denominador + self.denominador * obj.numerador 
      factor_denominador = self.den * obj.den
      fraccion_factor_de_dos_fracciones = Fraccion(factor_numerador, factor_denominador)
      fraccion_factor_de_dos_fracciones.simplifica()
      return fraccion_factor_de_dos_fracciones
    
    def __eq__(self, b):
      if self.numerador/self.denominador == b.numerador/b.denominador:
        return True
      else:
        return False
        
    def simplificaFracion(self):
        derivado = self.mcd(self.numerador, self.denominador)
        self.numerador = int(self.numerador/derivado)
        self.denominador = int(self.denominador/derivado)
        
    def mcd(self, a , b):
        if b == 0:
            return a
        else:
            return self.mcd(b, a%b)
     
    