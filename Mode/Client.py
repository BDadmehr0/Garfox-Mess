import socket
import threading

HOST = '127.0.0.1'
PORT = 5500

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

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

def send():
    while True:
        message = input()
        if message.startswith('/private '):
            recipient_name, message = message[9:].split(') ', 1)
            for client, props in properties.items():
                if props['name'] ==ادامه کد کلاینت: