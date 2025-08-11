#!/usr/bin/env python3

# Funciones
# def saludo(nombre):
#   print(f'Hola {nombre}')

# saludo('jose')

# Funciones lambda

cuadrado = lambda x: x**2

print(cuadrado(2))

numeros = [1,2,3,4,6,7,8]

print(numeros)

cuadrados = list(map(cuadrado, numeros))

print(cuadrados)
