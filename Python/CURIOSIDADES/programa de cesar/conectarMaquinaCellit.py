import subprocess
import sys

def conectar_ssh(usuario, contrasena, servidor):
    comando = f'sshpass -p {contrasena} ssh {usuario}@{servidor}'
    subprocess.run(comando, shell=True)

def obtener_credenciales(servidor):
    credenciales = {
        'EECC': {'usuario': 'cellit_eecc_dev_user', 'contrasena': '2023CitEECCBdi', 'direccion': '143.42.5.100'},
        'AMI': {'usuario': 'cellit_ami_dev_user', 'contrasena': '2023CitcLAmIBdi', 'direccion': '143.42.5.100'},
        'CASH': {'usuario': 'cellit_cashback_dev_user', 'contrasena': 'cellit_cashback_dev_user', 'direccion': '143.42.5.100'},
        'PCC': {'usuario': 'cellit_pcc_dev_user', 'contrasena': '2023CitCLPccBdi', 'direccion': '143.42.5.100'}
    }

    if servidor in credenciales:
        return credenciales[servidor]
    else:
        print("Nombre de servidor no reconocido.")
        sys.exit(1)

# Recibe el nombre del servidor como argumento de la línea de comandos
if len(sys.argv) != 2:
    print("Uso: python3 conectarMaquinaCellit.py <nombre_servidor>")
    sys.exit(1)

nombre_servidor = sys.argv[1]

credenciales = obtener_credenciales(nombre_servidor)

conectar_ssh(credenciales['usuario'], credenciales['contrasena'], credenciales['direccion'])
