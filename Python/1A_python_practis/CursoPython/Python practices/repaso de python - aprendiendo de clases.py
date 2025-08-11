# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 10:57:25 2023

@author: KraosFex
"""

# clases y Objetos.
# las clases son modelos que nos permiten contruir objetos.
# POO intenta abstraer lo mas importante de un objeto:

# Reglas Para construir una clase
    # Para toda clase en python debe existir un constructor __init__ 
    # Todo metodo de clase simpre, sin excepcion, recive como primer parametro self
    # Self es una referencial al objeto actual

# Metodos especiales para clases
    # __init__
    # __del__ <-- los casos de uso de este metodo no los veo muy claros
    # __str__ <-- Atravez de este metodo es la forma mas recomendable de imprimir valores, no usar print

# Sobre carga de operadores
    # Suma: __add__ +
    # Resta: __sub__ -
    # Multiplicacion: __mul__ *
    # Division: __div__ /
    # Igualdad: __eq__ ==
    # Menor que: __it__ <
    # Mayor que: __gt__ >

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
    
    # ejerciosos:
    ## A. Crear el metodo sumar
    ## Respuesta abajo de esta linera:
    
        
    ## B. Crear el metodo restar
    ## Respuesta abajo de esta linera:
        
    
    ## B. Crear el metodo dividir
    ## Respuesta abajo de esta linera:
    
    
    def imprime(self):
        print(self.num, '/', self.den)

def main():
    a = Fraccion(7, 8)
    a.imprime()

main()

# Ejemplo nuevo:
class Lampara01:
    _ESTADOS = ['Apagada', 'Encendida']
    
    def __init__(self, estado_inical):
        self.estado_actual = estado_inical 
    
    def ver_estado_lampara(self):
        if self.estado_actual == True:
            print(self._ESTADOS[1])
        else:
            print(self._ESTADOS[0])
    
    def encender(self):
        self.estado_actual = True
        self.ver_estado_lampara()
    
    def apagar(self):
        self.estado_actual = False
        self.ver_estado_lampara()
        
def main():
    lamp = Lampara01(False)
    menu = ''' Menu:
        0 > Apagar Lampara
        1 > Encender Lampara
        x > Salir'''
    while True:
        print(menu)
        op = input("Que opcion desea: ")
        if op == '0':
            lamp.apagar()
        elif op == '1':
            lamp.encender()
        else:
            break
            
main()    
    
    
## Correccion usando metodos de clases
class Lampara02:
    _ESTADOS = ['Apagada', 'Encendida']
    
    def __init__(self, estado_inical):
        self.estado_actual = estado_inical 
    
    def __str__(self):
        if self.estado_actual == True:
            return self._ESTADOS[1]
        else:
            return self._ESTADOS[0]
    
    def encender(self):
        self.estado_actual = True
    
    def apagar(self):
        self.estado_actual = False
    
def main():
    lamp = Lampara02(False)
    menu = ''' Menu:
        0 > Apagar Lampara
        1 > Encender Lampara
        x > Salir'''
    while True:
        print(menu)
        op = input("Que opcion desea: ")
        if op == '0':
            lamp.apagar()
            print(lamp)
        elif op == '1':
            lamp.encender()
            print(lamp)
        else:
            break
            
main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
