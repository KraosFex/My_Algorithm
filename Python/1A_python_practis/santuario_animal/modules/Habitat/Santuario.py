from .Bioma import Bioma

class SantuarioAnimal:
  def __init__(self, direccion, nombre,  tamano ) -> None:
    try:
      if tamano not in ["s", "m", "x"]:
        raise Exception(f"El tamaño del bioma solo puede ser pequeño, mediano o grande")
      else:
        self.tamano = tamano # pequeño media o grande
      self.nivel_de_santuario = 0
      self.direccion = direccion # Direccion del santuario
      self.nombre = nombre # Nombre del santuario
      self.espacio_ocupado = []
      self.biomas = {}
    except Exception as e:
      print(f"Nose puede generar el santuario:\n\t[Error]{e}")

  @property
  def espacio_disponible(self):
    if self.tamano == "s":
      return 4
    elif self.tamano == "m":
      return 8
    elif self.tamano == "x":
      return 12

  def agregar_bioma(self, bioma):
    if isinstance(bioma, Bioma):
      # if len(self.biomas) < self.espacio_disponible:
      if bioma.nombre in self.biomas:
        print(f"\n[!] El bioma {bioma.nombre} que intentas agregar ya existe en el santuario.")
        return
      else:
        if sum([bioma for bioma in self.espacio_ocupado]) < self.espacio_disponible:
          self.biomas[bioma.nombre] = bioma
          self.espacio_ocupado.append(bioma.disponibilidad_vivienda)
          print(f"\n[+] Bioma {bioma.nombre} agregado exitosamente, puedes agregarle {bioma.disponibilidad_vivienda} animales")
        else:
          print(f"\n[!] El numero maximo de biomas posibles en el santuario a sido alcansado.\n\tNo es poble agregar el bioma {bioma.nombre}.")
    else:
      print(f"\nEl bioma que se intenta agregar no es un objeto valido.")

  def retirar_bioma(self, bioma:str):
    if bioma in self.biomas:
      if self.biomas[bioma].cantidad_animales <= 0:
        obj = self.biomas.pop(bioma)
        self.espacio_ocupado.remove(obj.disponibilidad_vivienda)
        print(f"\n[+] el bioma {obj.nombre} fue removimo.")
      else:
        print(f"\n[!] El bioma que deseas eliminar debe estar innavitado, antes de ser eliminado.")
    else:
      print(f"\n[!] El bioma que intentas agregar no existe en el santuario.")

  @property
  def mostrar_biomas(self):
    info = "\n[+] Biomas disponibles en el santuario animal:"
    for bioma in self.biomas.values():
      info += f"\n\t\t\tBioma: {bioma.nombre}, capacidad: {bioma.disponibilidad_vivienda} animales"
    return info

  # ESTOY EVALUANDO SI ES NECESARIA ESTA FUNCIONALIDAD AQUI
  # def agregar_animal(self, bioma:str, animal:object):
  #   if bioma in self.biomas:
  #     self.biomas[bioma].agregar_animal(animal)
  #     return f"\n[+] {animal.nombre}, fue correcatamente agragado"
  #   else:
  #     return "\n[!] No se encuentra el bioma al que intentas agregar este animal."

  def __str__(self) -> str:
    datos = f"[+] Este es el santuario animal {self.nombre}"
    if len(self.biomas) == 0:
      datos += "\n\t[!] Aun no se han agregaso biomas al santuario animal."
    else:
      datos += f"{self.mostrar_biomas}"
    return datos
