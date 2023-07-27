import socket

def run_client():
    server_ip = '127.0.0.1'
    server_port = 12345

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))

    while True:
        message = input("Your message: ")
        client.send(message.encode('utf-8'))

    client.close()