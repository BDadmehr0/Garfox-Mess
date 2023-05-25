import socket
import threading

HOST = '127.0.0.1'  # آدرس IP محلی
PORT = 5500  # شماره پورت

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

clients = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            break

def start():
    server.listen()
    while True:
        client, address = server.accept()
        clients.append(client)
        print(f"Connected with {str(address)}")

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

print("Server is running...")
start()