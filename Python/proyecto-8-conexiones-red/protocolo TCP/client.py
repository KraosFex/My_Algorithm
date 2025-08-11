import socket

def connected_server():
  host = 'localhost'
  port = 12345
  add_conn = (host, port)

  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(add_conn)
    # print(f"\nServidor el escucha en {host}:{port}")
    s.sendall(b"Hola, servidor!")
    data = s.recv(1024)

  print(f"\n[+] Mensaje recibido del servidor:\n\t{data.decode()}")

connected_server()
