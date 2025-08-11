import os
import time

# Constantes
CONSRANG = 4
PRINCE = '@'
BACKGROUND_CHAR = '#'

# Inicialización
screen = [[BACKGROUND_CHAR for _ in range(CONSRANG)] for _ in range(CONSRANG)]
current_x, current_y = 0, 0

def clear_screen():
    """Limpia la pantalla de manera multiplataforma"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_screen():
    """Imprime la pantalla de manera eficiente"""
    for row in screen:
        print(''.join(row))
    print()  # Espacio adicional para mejor legibilidad

while True:
    # Actualiza la posición del personaje
    screen[current_x][current_y] = PRINCE

    # Muestra la pantalla
    clear_screen()
    print_screen()

    # Restaura la posición anterior a fondo
    screen[current_x][current_y] = BACKGROUND_CHAR

    # Actualiza coordenadas
    current_y += 1
    if current_y >= CONSRANG:
        current_y = 0
        current_x = (current_x + 1) % CONSRANG  # Usamos módulo para simplificar

    time.sleep(0.5)  # Reducido a 0.5s para mejor experiencia
