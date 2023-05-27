def main_client():
    import socket

    client_socket = socket.socket()
    port = 12345
    client_socket.connect(('127.0.0.1',port))

    #recieve connection message from server
    recv_msg = client_socket.recv(1024)
    print(recv_msg)

    #send user details to server
    send_msg = input("Enter your user name(prefix with #)")
    client_socket.send(send_msg.encode())

    #receive and send message from/to different user/s
    while True:
        recv_msg = client_socket.recv(1024)
        print(recv_msg.decode())  # تبدیل بایت به رشته و چاپ

        send_msg = input("Send your message in format [@user:message] ")
        if send_msg == 'exit':
            break
        else:
            client_socket.send(send_msg.encode())  # تبدیل رشته به بایت و ارسال به سرور

    client_socket.close()