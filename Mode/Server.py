import socket
import threading

HOST = '127.0.0.1'
PORT = 5500

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

clients = []
properties = {}

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client, address):
    properties[client] = {"address": address, "name": ""}
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message.startswith('/name '):
                name = message[6:]
                properties[client]["name"] = name
                message = f"{name} joined the chat!"
            elif message.startswith('/private '):
                recipient_name, message = message[9:].split(') ', 1)
                for client, props in properties.items():
                    if props['name'] == recipient_name:
                        recipient = client
                        message = f"(private message) {message}"
                        break
                else:
                    print("Recipient not found!")
                    continue
                recipient.send(f"{str(properties)}{message}".encode('utf-8'))
            broadcast(f"{str(properties)}{message}".encode('utf-8'))
        except:
            index = clients.index(client)
            clients.remove(client)
            del properties[client]
            client.close()
            break

def start():
    server.listen()
    print("Server isrunning...")
    while True:
        client, address = server.accept()
        clients.append(client)
        print(f"Connected with {str(address)}")

        thread = threading.Thread(target=handle_client, args=(client, address))
        thread.start()

start()