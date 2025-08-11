numeros = [1, 2, 3, 4, 5]
duplicar = lambda x: x * 2

# Aplicar la función lambda a cada elemento de la lista
resultado = list(map(duplicar, numeros))
print(resultado)  # Output: [2, 4, 6, 8, 10]

pares = lambda x: x % 2 == 0

# Filtrar los números pares
resultado = list(filter(pares, numeros))
print(resultado)  # Output: [2, 4, 6, 8]

personas = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
# Ordenar por edad (segundo elemento de la tupla)
ordenado = sorted(personas, key=lambda x: x[1])

print(ordenado)  # Output: [('Bob', 20), ('Alice', 25), ('Charlie', 30)]

