numeros = [-12, 84, 13, 20, -33, 101, 9]

# Completa el ejercicio aquí
def separar(lista_numerica):
    lista_de_pares = []
    lista_de_impares = []
    
    for numero in lista_numerica:
        if numero%2 == 0:
            lista_de_pares.append(numero)
            continue
        else:
            lista_de_impares.append(numero)
            continue
    return lista_de_pares, lista_de_impares

pares, impares = separar(numeros)

print(pares)
print(impares)