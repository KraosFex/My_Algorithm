#!/usr/bin/env python3

# Esta es mi manera de resolver el ejercio
# def array_diff(a, b):
#   new_list = []
#   for x in a:
#     if x not in b:
#       new_list.append(x)
#   return new_list

# Esta es una manera mas corta de hacerlo
def array_diff(a, b):
  return [x for x in a if x not in b]

print(array_diff([1, 1, 1, 1, 2], [2]))
