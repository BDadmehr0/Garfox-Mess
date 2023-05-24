import socket
import threading

# آدرس و پورت سرور
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 1234

# لیست کلاینت‌ها
clients = []

def handle_client(client_socket, client_address):
    while True:
        try:
            # دریافت پیام از کلاینت
            message = client_socket.recv(1024).decode()
            if message:
                print(f'{client_address}: {message}')
                # ارسال پیام به کلاینت‌های دیگر
                for client in clients:
                    if client != client_socket:
                        client.send(message.encode())
            else:
                # اگر کلاینت قطع شود، آن را از لیست کلاینت‌ها حذف کنید
                clients.remove(client_socket)
                client_socket.close()
                break
        except:
            # اگر خطایی رخ دهد، کلاینت را از لیست کلاینت‌ها حذف کنید
            clients.remove(client_socket)
            client_socket.close()
            break

