#!/usr/bin/env python3

# Manejo de errores y excepciones
try:
  num = 3/0
except ZeroDivisionError:
  print("No es posible dividir entre cero")
else:
  print("Bien")
finally:
  print("Siempre verifica que le valor no es 0")
