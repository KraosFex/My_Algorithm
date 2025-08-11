def crea_cubo(n):
    for x in range(n):
        yield(x**n)
        
        
for x in crea_cubo(10):
    print(x)