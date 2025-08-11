# Ejemplo 1
while True:
  try:
    edad = int(input(f"Dime tu edad: "))
    print(f"Tu edad es {edad}")
    break
  except ValueError:
    print(f"El Dato introducido es incorrecto")

#Ejemplo 2
from getpass import getpass
psw = getpass(f"Introduce tu contraseña: ")
print(f"Tu contraseña es: ")
