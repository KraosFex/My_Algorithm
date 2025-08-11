import os
import time

# NO ENTIENDO POR QUE NO FUNCIONA COMO YO SIEMPRE HE PENSADO QUE FUNCIONA,
# PUEDE SER POSIBLE QUE SIEMPRE E ALLA EQUIVOCADO

CONSRANG = 4
CURRENT_X = 0
CURRENT_Y = 0
PRINCE = "@" 

os.system('clear')

sub_background = ["#"]*CONSRANG
background = [sub_background]*CONSRANG

screen = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

def repain_screem():
    for i in range(CONSRANG):
        for j in range(CONSRANG):
            screen[i][j] = background[i][j]

repain_screem()

while True:
    screen[CURRENT_X][CURRENT_Y] = PRINCE

    for i in range(CONSRANG):
        print(f"{''.join(screen[i])}")

    time.sleep(1);

    os.system('clear');

    CURRENT_Y += 1;

    if CURRENT_Y > (CONSRANG - 1):
        CURRENT_Y = 0;
        CURRENT_X += 1;
        if CURRENT_X > (CONSRANG - 1):
            CURRENT_X = 0;

    repain_screem()

