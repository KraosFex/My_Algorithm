import sys

def imprime_tablas_de_multiplicar(numero_de_tablas_que_quieres_ver):
    for n in range(int(numero_de_tablas_que_quieres_ver ) + 1):
        print('')
        for j in range(11):
            print(f"{n}x{j}={n*j}")

def imprime():
    if len(sys.argv) == 2:
        imprime_tablas_de_multiplicar(sys.argv[1])          
    else:
        print("Error: argumento invalido\n\tejemplo: tablas_de_multiplicar.py [algun numero entero positivo]")

    
imprime()
