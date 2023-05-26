import subprocess
import json
import datetime

def log():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hostname = subprocess.check_output(['hostname']).decode().strip()
    os = subprocess.check_output(['uname']).decode().strip()

    data = {
        "name": "Garfox-mess",
        "version": "0.0.1",
        "production-date": "2023-05-26",
        "last-update": now,
        "system": {
            "OS": os,
            "host": hostname
        }
    }

    with open('./log/install.json', 'w') as f:
        json.dump(data, f)

def log_loader():
    def installation():
        print("Installing python3-pip...")
        subprocess.check_call(['apt-get', 'install', '-y', 'python3-pip'])

        print("Installing python3...")
        subprocess.check_call(['apt-get', 'install', '-y', 'python3'])

        print("Installing required packages...")
        subprocess.check_call(['pip3', 'install', '-r', 'requirements.txt'])

        print("Copying Garfox-mess to /opt...")
        subprocess.check_call(['cp', '-r', './Garfox-mess', '/opt/Garfox-mess'])

        print("Creating symlink...")
        subprocess.check_call(['ln', '-s', '/opt/Garfox-mess/GM.py', '/usr/local/bin/myapp'])

        print("Starting Garfox-mess...")
        subprocess.check_call(['python3', '/opt/Garfox-mess/GM.py'])

        print("Installation completed.")

    try:
        with open('./log/log.json', 'r') as f:
            log_load = f.read()
            if not log_load:
                print("Log file not found. Creating new log file.")
                installation()
            else:
                y_str = ['y','Y','yes','YES','Yes','yEs','yeS']
                while True:
                    qus_agin = input("Log file found. You have already installed I want to install it again ? [y/N]")
                    if qus_agin in y_str:
                        log()
                    else:
                        print('Install Done')
                        exit()


    except FileNotFoundError:
        print("Log file not found. Creating new log file.")
        installation()

log_loader()
log()
