#!/bin/bash

log () {
    version = "1.0.0"
    furme = ""
}

log_loader () {
    clear
    log_load = cat ./log/s.json

    if [ $log_load == "" ]
    then
        echo "Crate Log"
        log
    fi
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