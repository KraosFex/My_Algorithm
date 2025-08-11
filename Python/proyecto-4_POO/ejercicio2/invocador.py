from super.Producto import Producto
from sub.Adorno import Adorno


a = Adorno("#7875dd", "Casa de Muñecas", 15, "Una linda casita de muñecas con la que puede jugar tus niñas")
b = Adorno("#7875AA", "Muñeca1", 5, "oiidfnkkps kdk kdkjdikd kj kjsdaifj kd sikis")
c = Adorno("#787R88", "Muñeca2", 15, "dfidsjfasi jasdfas disofjsa ji jidasfjan")
d = Adorno("#7965SD", "Pista de carrerras", 41, "hfdhfiuhdufahdfs")


lista_de_productos = []

lista_de_productos.append(a)
lista_de_productos.append(b)
lista_de_productos.append(c)
lista_de_productos.append(d)

for producto in lista_de_productos:
    print(f"\n{producto}")

