#!/usr/bin/env python3
import os
from Control import UserManagement
from modules import Animal, SantuarioAnimal

class Create_menu():
    def new_options(list_options:tuple) -> str:
        menu = ""
        for option in list_options:
            menu += f"[+] {option}\n"
        print(menu)

class Create_form():
    pass

def nuevo_animal():
      especie = input("\nIntroduce la especie del animal: ")
      nombre_animal = input(f"Introduce el nombre del {especie}: ")
      edad_animal =int(input(f"Introduce edad del {especie}: "))
      tamano_animal =int(input(f"Introduce el tamaño del {especie}(cm): "))
      peso_animal =int(input(f"Introduce el peso del {especie}(kg): "))
      return Animal(especie, nombre_animal, edad_animal, tamano_animal, peso_animal)

list_options_init = ("Iniciar sesion (preciona <1>)", 
                     "Registrarse (preciona <2>)",
                     "Salir (preciona <x>)")

class App:
    def __init__(self):
        pass

    def log_in(self, credentials):
        res = GestorUsuarios.login_user(credentials)
        if res["status"] == True:
            self.userdate = res["user"]
        elif res["status"] == False:
            raise Exception("[!] Not register user.")
        else:
            raise Exception("[!] Algo salio mal.")

    def register_user(self, credentials_new_user:tuple) -> bool:
        result = GestorUsuarios.nuevo_usuario(credentials_new_user)
        return result

def main():
  input("\n[+] Bienvenido, preciona <enter> para comenzar.")
  os.system("cls" if os.name == "nt" else "clear")
  run = App()

  # gestor_usuario = GestorUsuarios()
  sesion = 0
  while True:
    Create_menu.new_options(list_options_init)
    option = input("\n[+] Que eleccion deseas tomar: ")

    if option == "1":
      usuario = input("[+] Usuario: ")
      clave = input("[+] Clave: ")
      run.login_user((usuario, clave))

    elif option == "2":
      usuario = input("[+] Usuario: ")
      contrasena = input("[+] Contraseña: ")
      result = run.register_user((usuario, contrasena))
      
      if result == True:
          print("\n[+] El registro fue completado exitosamente.\n")
      else:
          print("\n[!] No es posible registrar un nuevo usuario.\n")
    elif option == "x":
      print("\nHasta la proxima!")
      break

    else:
      print("\n[!] '{option}' no es una eleccion valida.")

    input("\nPreciona <enter> para continuar.")
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
  main()
