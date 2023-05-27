def main_client():
    import socket
    import threading

    HOST = '127.0.0.1'
    PORT = 5510

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))
    except ConnectionRefusedError:
        print('The server is currently unavailable or the port specified to connect to the server is incorrect')

        for i in range(5): # Time Out 5 again
            rety = input('try again y/N :')
            if rety == 'y':
                try:
                    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    client.connect((HOST, PORT))
                except ConnectionRefusedError:
                    print('The server is currently unavailable or the port specified to connect to the server is incorrect')
            else:
                exit()
        exit()
            

    def receive():
        while True:
            message_recv = client.recv(1024).decode('utf-8')
            print(f"{message_recv}")

    def send():
        while True:
            message_send = input('Client-Message $: \n')
            if message_send == 'exit':
                client.close()
                exit()
            else:
                client.send(f"{message_send}".encode('utf-8'))

    receive_thread = threading.Thread(target=receive)
    send_thread = threading.Thread(target=send)

    receive_thread.start()
    send_thread.start()