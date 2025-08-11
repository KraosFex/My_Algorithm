
# Me esta comiendo la vida todos estos ejercicio...

# Crear una función llamada divisores/Divisores que toma un entero n > 1 
# y devuelve una matriz con todos los divisores del entero 
# (excepto 1 y el propio número), de menor a mayor.

def divisors(n):
    results = []
    for val in range(n):
        if val < 2:
            continue
        elif n%val == 0:
            results.append(val)
    if len(results) < 1:
        return f"{n} is prime"
    return results

print(divisors(10))
print(divisors(345))
print(divisors(13))
