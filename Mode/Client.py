import socket
import threading

HOST = '127.0.0.1'  # آدرس IP محلی
PORT = 5500  # شماره پورت

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Error occurred!")
            client.close()
            break

def send():
    while True:
        message = input()
        client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=receive)
send_thread = threading.Thread(target=send)

receive_thread.start()
send_thread.start()