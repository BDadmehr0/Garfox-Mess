from mods.server import run_server
from mods.client import run_client

print('\n(1) Server\n(2) Client\n\n(00) Exit\n')

if __name__ == "__main__":
    Q = input('-> ')

    if Q == '1':
        run_server()
    elif Q == '2':
        run_client()
    elif Q == '00':
        print('\n\n')
        exit()
    else:
        print(f'\n{Q}: Fail Command\n')