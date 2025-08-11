#!/bin/bash

####################################################
## Autor: Ing. César Fernández                    ##
## Utilidad que permite conectarme por ssh        ##
## al server cellit con los diferentes User       ##
##                                                ##
####################################################

# Verifica que se proporciona un nombre de servidor
if [ -z "$1" ]; then
    echo "Por favor, proporciona un nombre de servidor."
    exit 1
fi

# Nombre del servidor que se pasa como argumento
nombre_servidor=$1

# Ruta completa a sshpass
ruta_sshpass=$(which sshpass)

# Ruta al script de Python
python_script="/home/cesarf/Curso/Pyhton/conectarMaquinaCellit.py"

# Ejecuta el script de Python con el nombre del servidor como argumento
"$ruta_sshpass" -p "${credenciales["contrasena"]}" ssh "${credenciales["usuario"]}"@"$nombre_servidor"

python3 "$python_script" "$nombre_servidor"
