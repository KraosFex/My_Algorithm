import socket
import threading

class ClientThread(threading.Thread):
  def __init__(self, client_sock, client_addr):
    super().__init__()
    self.client_sock = client_sock
    self.client_addr = client_addr

    print(f"\n[+] Nuevo cliente conectado: {self.client_addr}")

  def run(self):
    msg = ''
    while True:
        data = self.client_sock.recv(1024)
        msg = data.decode().strip()
        if msg == "bye":
          break
        print(f"\n[+] Mensaje enviado por {self.client_addr}:\n\t\t{msg}")
        self.client_sock.send(data)

def start_server():
  HOST = 'localhost'
  PORT = 12345
  add_conn = (HOST, PORT)

  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(add_conn)
    print(f"\nServidor el escucha en {HOST}:{PORT}")

    while True:
      server_socket.listen()
      client_sock, client_addr = server_socket.accept()
      new_thread = ClientThread(client_sock, client_addr)
      new_thread.start()


start_server()
