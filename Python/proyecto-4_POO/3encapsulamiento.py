
# # Encapsulamiento
# class Ejemplo:
#   def __init__(self):
#     self._x = 'x'# atributo protegido
#     self.__x = 'xx' # atributo privado, aplica name mangling
#                     # se puede acceder como:
#                       # _(nombre de la clase)__(nomber tributo privado)
#                       # _Ejemplo__x <= Esto aplica para todos atributos privados

# # Metodos especiales a de clases;

# # Los métodos especiales en Python son también conocidos como métodos mágicos y son identificados por doble guion bajo al inicio y al final (‘__metodo__‘). Permiten a las clases en Python emular el comportamiento de los tipos incorporados y responder a operadores específicos. Por ejemplo, el método ‘__init__‘ se utiliza para inicializar una nueva instancia de una clase, ‘__str__‘ se invoca para una representación en forma de cadena legible del objeto y ‘__len__‘ devuelve la longitud del objeto.

# # Algunos métodos especiales importantes en POO son:

# # __init__(self, […]): Inicializa una nueva instancia de la clase.
# # __str__(self): Devuelve una representación en cadena de texto del objeto, invocado por la función ‘str(object)‘ y ‘print‘.
# # __repr__(self): Devuelve una representación del objeto que debería, en teoría, ser una expresión válida de Python, invocado por la función ‘repr(object)‘.
# # __eq__(self, other): Define el comportamiento del operador de igualdad ‘==‘.
# # __lt__(self, other), __le__(self, other), __gt__(self, other), __ge__(self, other): Definen el comportamiento de los operadores de comparación (<, <=, > y >= respectivamente).
# # __add__(self, other), __sub__(self, other), __mul__(self, other), etc.: Definen el comportamiento de los operadores aritméticos (+, –, *, etc.).


# # Propiedades de decoradores
# class Persona:
#   def __init__(self, edad):
#     self._edad = edad

#   @property #Getter Por que accede al atributo privado
#   def edad(self):
#     return self._edad

#   @edad.setter # Setter por que modifica el atributo privado
#   def edad(self, x): # Mantiene el mismo nombre que el property definifo anteriormente y recibe un argumento
#     self._edad = x

# # Argumentos de una funcion
# import time
# # *args es para argumentos posicionales
# # **kwargs es para pares clave valor

# def pausa(*args, **kwargs):
#   for num in args:
#     time.sleep(num)
#     print(f"pausa que duro: {num}")

# pausa(2,3,4,5,6,7,7)
