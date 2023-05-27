def main_server():
    import socket
    import threading
    from colorama import Fore, Style
    import os
    import urllib.request

    def get_public_ip():
        url = 'https://api.ipify.org'
        response = urllib.request.urlopen(url)
        ip = response.read().decode()
        return ip

    # localhost 127.0.0.1
    HOST = get_public_ip()
    PORT = 5050

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
                    os.system('sudo lsof -i :5510')
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