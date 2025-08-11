#!/usr/bin/env python3

import socket

def start_udp_client():
  host = 'localhost'
  port = 1234
  addr_conn = (host, port)

  with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(b"Buenas tardes", addr_conn)

start_udp_client()
