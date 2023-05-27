def main_server():
    import socket
    import threading
    from colorama import Fore, Style
    import os

    # localhost 127.0.0.1
    HOST = '127.0.0.1'
    PORT = 5510

    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, PORT))
    except OSError:
        print('Port Error: plase enter password and auto change port')
        os.system('sudo lsof -i :5510')

        for i in range(5): # Time Out 5 again
            rety = input('try again y/N :')
            if rety == 'y':
                try:
                    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    server.bind((HOST, PORT))
                except OSError:
                    print('Port Error: plase enter password and auto change port')
            else:
                exit()
        exit()


    def recv(client):
        while True:
            message_recv = client.recv(1024).decode('utf-8')
            print(f"{message_recv}")


    def send(client):
        while True:
            message_send = input('Host-Message $:\n ')
            if message_send == 'exit':
                client.close()
                exit()
            else:
                client.send(f"{message_send}".encode('utf-8'))


    def start():
        server.listen()
        print("Server " + Fore.GREEN + Style.BRIGHT + "Online")

        while True:
            client, address = server.accept()
            print(f"join {str(address)}")

            thread1 = threading.Thread(target=recv, args=(client,))
            thread2 = threading.Thread(target=send, args=(client,))

            thread1.start()
            thread2.start()


    start()