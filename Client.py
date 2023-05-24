import socket
import thrading

target_host = "127.0.0.1"
target_port = 1234

client = []

def handel_client():
  while True:
    try:
      mesage = client_socket.recv(1024).decode()
