# Podemos utilizar la función enumerate() 
# para conseguir el índice y el valor en cada iteración fácilmente:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for indice,numero in enumerate(numeros):
    numeros[indice] *= 10

print(numeros)

for indice in enumerate(numeros):
    print(indice[1])
    
cadena = "hola mi loco"

cadena2 = ""
for caracter in cadena:
    cadena2 += caracter * 2

print(cadena2)