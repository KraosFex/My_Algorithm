# Todo movimiento es un simulacion que ocurre de forma muy rapida
# un elemento de un punto A se elimina y se crea en un punto B
#
#   Ejemplo:
#
#       [^,^,^,^,@,^,^,^] -----> moviento de @ -------> [^,@,^,^,^,^,^,^]
#
#   Ejemplo de codigo

background = [1, 1, 2, 2, 2, 1] # Este sera nuestro fondo 
screen = [0]*6 # Este sera la pantalla en blanco que renderizara nuestro fondo

# Con este bucle dibujamos nuestro fondo en nuesta pantalla en blanco
for i in range(6):
    screen[i] = background[i]
print(screen) #[1, 1, 2, 2, 2, 1]

# Esta es la posicion del elemento que se movera por la pantalla
playerpos = 3

# Asignamos el elemento a su posicion inicial dentro de la pantalla
screen[playerpos] = "@"
print(screen) # [1, 1, 2, "@", 2, 1] <- el elemento ocupa el lugar indicado por nosotros

# Para hacer que se mueva "@" hay que borrarlo de la posicion A y luego pintarlo en la posicion B
# Primero borramos al elemento playerpos, reescribiendo screen, con lo que tiene background en la posicion
# que ocupa playerpos
screen[playerpos] = background[playerpos]

playerpos = playerpos - 1

screen[playerpos] = "@"

print(screen)

screen[playerpos] = background[playerpos]

playerpos = playerpos - 1

screen[playerpos] = "@"

print(screen)
