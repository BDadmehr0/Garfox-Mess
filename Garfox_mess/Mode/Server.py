def main_server():
    import socket
    import threading
    from colorama import Fore,Style

    HOST = '127.0.0.1'
    PORT = 5510

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    

    def recv(client):
        while True:
            message_recv = client.recv(1024).decode('utf-8')
            print(f"{message_recv}")

    def send(client):
        while True:
            message_send = input('Host-Message $: ')
            client.send(f"{message_send}".encode('utf-8'))

    def start():
        server.listen()
        print("Server "+Fore.GREEN+Style.BRIGHT+"Online")

        while True:
            client, address = server.accept()
            print(f"Connected with {str(address)}")

            thread = threading.Thread(target=recv, args=(client,))
            thread2 = threading.Thread(target=send, args=(client,))
            thread.start()
            thread2.start()

    start()