import socket
import threading

clients = {}  # Dictionary to keep track of connected clients and their addresses

def handle_client(client_socket, client_address):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Received message from {client_address}: {message}")
            broadcast_message(message, client_socket)
        except Exception as e:
            print(f"Error: {e}")
            break

    # Client disconnected, remove from the connected clients dictionary
    del clients[client_socket]
    client_socket.close()

def broadcast_message(message, sender_socket):
    for client_socket in clients:
        if client_socket != sender_socket:
            try:
                client_socket.send(message.encode('utf-8'))
            except Exception as e:
                print(f"Error sending message: {e}")
                # If there's an error sending the message to a client, remove it from the dictionary
                del clients[client_socket]
                client_socket.close()

def run_server(server_ip, server_port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, server_port))
    server.listen(5)

    print(f"[*] Listening on {server_ip}:{server_port}")

    while True:
        client_socket, client_address = server.accept()
        print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")

        # Add the new client to the connected clients dictionary
        clients[client_socket] = client_address

        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()