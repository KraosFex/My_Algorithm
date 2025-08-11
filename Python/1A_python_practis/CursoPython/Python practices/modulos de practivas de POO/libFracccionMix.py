# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 22:11:17 2023

@author: KraosFex
"""

from libFracccion import Fraccion

class FracMix(Fraccion):

    def __init__(self, parteEntera, numeradorFraccionario=0, denominadorFraccionario=1):
        self.parteEntera=parteEntera
        super().__init__(numeradorFraccionario, denominadorFraccionario)    
        self.simplifica()
        super().simplifica()

    def __str__(self):
        return str(self.parteEntera) + super().__str__()

    def simplifica(self):
        if self.numeradorFraccionario > self.denominadorFraccionario:
            aux = self.numeradorFraccionario//self.denominadorFraccionario
            self.parteEntera=self.parteEntera + aux
            self.numeradorFraccionario -= (aux*self.denominadorFraccionario)
    
    def __add__(self, obj):
        ent=self.ent+obj.ent
        f = super().__add__(obj)
        r = FracMix(ent,f.num,f.den)
        return r
    
    
primeraFraccionMixta = FracMix(3,4,5)

print(primeraFraccionMixta)
