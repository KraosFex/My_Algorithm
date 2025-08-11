#Manejando errores

def divicion_entre_cero():
    try:
        resultado = 10/0
    except Exception as e:
        print(f"Error: {e}")

divicion_entre_cero()
