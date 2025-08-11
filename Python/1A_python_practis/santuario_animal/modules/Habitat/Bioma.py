class Bioma:
  def __init__(self, nombre, tamano) -> None:
      try:
        if tamano not in ["s", "m", "x"]:
          raise Exception(f"El tamaño del bioma solo puede ser pequeño, mediano o grande")
        else:
          self.tamano = tamano # pequeño media o grande
        self.nombre = nombre
        self.__animales = {}
        self.candidad_animales_en_el_bioma = 0
      except Exception as e:
        print(f"Nose se puede generar el bioma:\n\t[Error]{e}")

  @property
  def disponibilidad_vivienda(self):
    if self.tamano == "s":
      return 2
    elif self.tamano == "m":
      return 4
    elif self.tamano == "x":
      return 6

  def agregar_animal(self, animal):
    if isinstance(animal, Animal):
      if len(self.__animales) < self.disponibilidad_vivienda:
        self.candidad_animales_en_el_bioma += 1
        self.__animales[animal.especie] = animal
        print(f"\n[+] Fue agregado {animal.nombre} al bioma {self.nombre}")
      else:
        print(f"\n[!] No es posible añadir a {animal.nombre} ya que se a alcanzado el tamaño maximo de vivienda.")
    else:
      print("\n[!] Lo que intentas añadir al bioma no es un animal.")

  def liverar_animal(self):
    pass

  @property
  def listar_animales_en_cautiverio(self):
    info = f"\n[+] En el bioma {self.nombre} hay un total de {len(self.__animales)} animales:"
    for animal in self.__animales:
      info += f"\n----------------------------------\n\t{animal.especie}: {animal.nombre} - {animal.edad} años"
    return info

  @property
  def cantidad_animales(self):
    return len(self.__animales)
