import socket
import argparse

def run_client(server_ip, server_port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))

    while True:
        message = input("Your message: ")
        client.send(message.encode('utf-8'))

    client.close()