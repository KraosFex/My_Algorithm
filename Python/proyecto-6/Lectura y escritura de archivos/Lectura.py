# Escritura
escribe = open("Example.txt", "w")
escribe.write("Primera linea de texto")
escribe.close()

# Añadir a algo que ya contenga codigo
añade = open("Example.txt", "a")
añade.write("\nSegunda linea de texto")
añade.close()

# Lectura
lee = open("Example.txt", "r")
leido = lee.read()
print(leido)
escribe.close()

# Hay una forma mucho mas obtima de hacer esto
with open("Example.txt", "w") as w:
  w.write("Texto")

with open("Example.txt", "a") as a:
  a.write("\nNueva linea de texto")

# esta sigue sin ser la forma mas eficiente de leer un archivo, que que cargas todo su contenido directamenet en memoria y esto podria causar que el scrip cargue sumamente lente si el archivo a leer es muy grande
with open("Example.txt", "r") as r:
  file_reading = r.read()

print(file_reading)

# La manera mas eficiente de leer un archivo, es la sigueinte:
with open("Example.txt", "r") as r:
  for line in r:
    print(line.strip()) # El strip es para que no aplique ningun tipo se salto de linea

# Cuando trataba con archivos de tipo binario, utilizamos "rb"
with open("Example.txt", "rb") as r:
  for line in r:
    print(line.strip().decode()) # El decode() es para decodificar la linea binaria

# Tambien al momento de hace una operatoria de escritura, es combeniente, hacerlo dentro de un try except, ya que puede darse el caso donde el archivo del que se busca leer no exista
try:
  with open("Example2.txt", "r") as r:
    print(r.read())
except FileNotFoundError:
  print("[!] No es posible encontrar este archivo")
