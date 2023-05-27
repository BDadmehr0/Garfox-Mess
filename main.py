from Garfox_mess.Mode.Server import main_server
from Garfox_mess.Mode.Client import main_client
import urllib.request
import socket
from colorama import Fore, Style
import os

class main:
    def Banner():
        def get_local_ip():
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            return local_ip
        
        def get_public_ip():
            url = 'https://api.ipify.org'
            response = urllib.request.urlopen(url)
            return response.read().decode('utf-8')

        public_ip = get_public_ip()
        local_ip = get_local_ip()

        print(f'''
        Welcome '''+Fore.RED+Style.BRIGHT+'''Garfox '''+Fore.WHITE+Style.BRIGHT+'''Messanger V1.0.0
        Created by Dadmehr With coffee
        Your IP Public'''+Style.BRIGHT+''' {public_ip} Local '''+Style.BRIGHT+'''{local_ip}\n''')

    
    def open_mode():
        host_mode_str = ['Host','host','h']
        client_mode_str = ['Client','client','c']

        mode = input('select Mode [Host / Client]\n:')
        if mode in host_mode_str:
            os.system('clear')
            print('Mode = Host')
            open_server = main_server()
        elif mode in client_mode_str:
            os.system('clear')
            print('Mode = Client')
            open_client = main_client()
        else:
            exit()

if __name__ == "__main__":
    os.system('clear')
    main.Banner()
    main.open_mode()
