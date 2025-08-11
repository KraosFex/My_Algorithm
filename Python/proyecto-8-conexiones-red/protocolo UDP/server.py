#!/usr/bin/env python3

import socket

def start_udp_server():
  host = 'localhost'
  port = 1234
  addr_conn = (host, port)
  # UDP
  with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(addr_conn)
    print(f"\n[+] Servicio UDP iniciado en {host}:{port}")

    while True:
      data, addr = s.recvfrom(1024)
      print(f"\n[+] Mensaje enviado por el cliente:\n\t{data.decode()}")
      print(f"[+] Informacion del cliente que nos ha enviado el mensaje: {addr}")
