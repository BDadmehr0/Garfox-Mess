#!/bin/bash

log () {
    echo LOG
}

log_loader () {
    
    log_load=$(cat ./log/log.json)

    if [ -z "$log_load" ]
    then
        echo "Create Log"
    else
        echo "Log Load"
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

log_loader