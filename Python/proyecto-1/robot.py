def menuDeUsuario():
    print("""Elige una opcion: \n 1. Preguntar algo \n 2. Prdecir el futuro \n 3. salir""")

def roboto():
    menuDeUsuario()
    while True:
        opcion = input("coloca un numero > ")
        if opcion == "1":
            pregunta = input("Has cualquier pregunta > ")
            print("Tu pregunta fue: " + pregunta, "\n La verdad es que nose")
        if opcion == "2":       
            print("Tu futuro sera muy triste")
        if opcion == "3":
            break        
        else:
            print("Elige una opcion valida")
            continue
roboto()    