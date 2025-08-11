def fizzBuzz():
    contenedor_de_valores = []
    for n in range(101):
        if n%3==0 and n%5==0:
            contenedor_de_valores.append('FizzBuzz')
            continue
        if n%3==0:
            contenedor_de_valores.append('Fizz')
        if n%5==0:
            contenedor_de_valores.append('Buzz')
        else:
            contenedor_de_valores.append(n)
    return contenedor_de_valores

def imprimir_valores():
    resultados = fizzBuzz()
    for valor in resultados:
        print(f"{valor} ", end='')
    
        
imprimir_valores()
