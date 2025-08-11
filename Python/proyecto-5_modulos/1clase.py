# La clase trata de la modularizacion de codigo en python utilizando import


# Redescubriendo cosas:
# Con el comando dir(<nombre del modulo>) se puede listar sus metodos y propiedades

# Hay modulo que vienen integrados al propio python y se les llama:
# "Builtin modules"
# La forma de importarlos para ver como se llaman y cuales son, es la siguiente:
import sys
print(sys.builtin_module_names)


# Para ver la ubicacion de un modulo no incorporado de python se hace con __file__
import hashlib
print(hashlib.__file__)

# library hijacking, se trata del secuestro de modulos de python
