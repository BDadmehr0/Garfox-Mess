import argparse

from mods.server import run_server
from mods.client import run_client

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Messenger Server")
    parser.add_argument('-mod', type=str, help='Select Your service Mod | server & client')
    parser.add_argument('--ip', type=str, default='127.0.0.1', help="Server IP address")
    parser.add_argument('--port', type=int, default=12345, help="Server port")
    args = parser.parse_args()

    if args.mod == 'server':
        run_server(args.ip, args.port)
    else:
        run_client(args.ip, args.port)
