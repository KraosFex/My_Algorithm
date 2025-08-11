#!/usr/bin/env python3

# Typos de datos primitivos
string = "my string"
number = 32
floating = 32.3

print(type(string))
print(type(number))
print(type(floating))

# Structuras de datos
# Listas
my_ports = []


# Operatoria con datos


first = 'cloro'

print(first[:2]*8 + first[2:])


# Operacion de listas
odd_numbers = [1,3,5,7,9]
even_numbers = [2,4,6,8,10]

result = map(sum, zip(odd_numbers, even_numbers))

for i in result:
  print(i)


#Ternario
edad = 18
result = "Eres mayor" if edad >= 18 else "eres aun muy joven"
print(result)
