#!/bin/bash

log () {
    echo Create Log
}

log_loader () {
    clear
    cat ./log/s.json
}

installion () {
    apt-get install -y python3-pip
    apt-get install -y python3


    pip3 install -r requirements.txt

    cp -r ./Garfox-mess /opt/Garfox-mess

    ln -s /opt/Garfox-mess/GM.py /usr/local/bin/myapp

    python3 /opt/Garfox-mess/GM.py

    echo "Install Done"
}

installion

log_loader

log