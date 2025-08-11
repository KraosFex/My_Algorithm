# [Avanzado] Crea un script llamado descomposicion.py que realice las siguientes tareas:

# Debe tomar 1 argumento que será un número entero positivo.
# En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.
# ** El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... tal que por ejemplo si se introduce el número:**

# > 3647
#** El programa deberá devolver una descomposición línea a línea como la siguiente utilizando las técnicas de formateo: **

#> 0007
#  0040
#  0600
#  3000
# Pista: Que el valor sea un número no significa necesariamente que deba serlo para formatearlo. 
# Necesitarás jugar muy bien con los índices y realizar muchas conversiones entre tipos cadenas, números y viceversa

import sys

if len(sys.argv) > 1:
    magnitud = len(sys.argv[1])
    value_inverido = sys.argv[1][::-1]
    contador = 1
    for n in range(magnitud):
        posicion = int(value_inverido[n]) * contador
        print(f"{posicion:0{magnitud}d}")
        contador *= 10
else:
    error_algoritmo = "\tError: Debes pasar como minimo un valor numerico\n\t\tejemplo:\n\t\t.\descompocicion.py 5"
    print(f"{error_algoritmo}")
