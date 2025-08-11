from random import *

numeros_de_ruleta = ["00", "0"] + list(range(1, 37))

n = 0
while (n < 38):
    index = randint(0, 37)
    ganador = numeros_de_ruleta[index]
    print(f'[+] El numerio ganador es: {ganador}')
    n += 1
