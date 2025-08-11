personajes = []
p = {'Nombre':'Gandalf','Clase':'Mago','Raza':'Humano'}
personajes.append(p)
p = {'Nombre':'Legolas','Clase':'Arquero','Raza':'Elfo'}
personajes.append(p)
p = {'Nombre':'Gimli','Clase':'Guerrero','Raza':'Enano'}
personajes.append(p)

### asi no funciona
# for p in personajes:
#     for c, v in p.items():
#         print(v, v, v)

for p in personajes:
    print(p['Nombre'],p['Raza'], p['Clase'])
