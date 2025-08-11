# una lista se arma con []

esto_es_una_lista = [1, 1,1,1,2, 3, 4, 5, 6, 7, 8, 9]
print(esto_es_una_lista[0])

# una tuplas se arma con ()

esto_es_una_tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# un conjunto desordenado se crea con {}

esto_es_un_conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Es muy util convertir listas en conjuntos para eliminar elementos duplicados

# Para convertir una lista es conjuntos se puede usar la funcion set()
lista1 = [1, 1, 1, 2, 2, 3, 4, 4, 4 ]

conjunto1 = set(lista1)

lista2 = list(conjunto1)

print(lista1)
print(conjunto1)
print(lista2)
print(lista1)

# se puede limpiar los elementos repetidos de una lista en una sola linea de la siguiente manera

lista3 = [1, 1, 1, 2, 2, 3, 4, 4, 4 ]
lista_limpiada = list(set(lista3))
print(lista_limpiada)
