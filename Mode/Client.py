import socket
import threading

HOST = '127.0.0.1'
PORT = 5500

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
        try:
            message = client.recv(1024).decode('utf-8')
            properties_start = message.find("[")
            properties_end = message.find("]")
            if properties_start != -1 and properties_end != -1:
                properties_str = message[properties_start:properties_end+1]
                properties = eval(properties_str)
                message = message[:properties_start] + message[properties_end+1:]
                print(f"{properties['name']} ({properties['address'][0]}:{properties['address'][1]}): {message}")
            else:
                print(message)
        except:
            print("Error occurred!")
            client.close()
            break

def send(client, properties):
    while True:
        message = input()
        if message.startswith('/private '):
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
        else:
            client.send(f"{str(properties)}{message}".encode('utf-8'))

properties = {'name': 'Client', 'address': (HOST, PORT)}

receive_thread = threading.Thread(target=receive)
send_thread = threading.Thread(target=send, args=(client, properties))

receive_thread.start()
send_thread.start()