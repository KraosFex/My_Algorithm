import sys

if len(sys.argv) > 1:
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])
    for r in range(repeticiones):
        print(texto)
else:
    print("\tLos argumentos son incorrectos: \n\t Ejemplo: \n\t .\escribiendo_lineas.py \"Hola mundo\" 10")
