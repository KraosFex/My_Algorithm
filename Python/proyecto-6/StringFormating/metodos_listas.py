cadena =  "Hola mundo como estas"

lista1 = cadena.split(" ")

lista1.insert(0,"--")
lista1.insert(len(lista1),"--")

lista1.reverse()

print(lista1)

cadena2 = "".join(lista1)

lista2 = list(cadena2)

lista2.reverse()

cadena3 = "".join(lista2)

print(cadena3)
