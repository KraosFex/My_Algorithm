# el operador walrus nos permite declarar y evaluar una variable al mismo tiempo.
# forma menos eficiente
def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

[print(factorial(i)) for i in range(1, 100)]

# forma eficiente utilizando el operador walrus
factor = 1
lista = [factor := factor*i for i in range(1,100)]
[print(n) for n in lista]
