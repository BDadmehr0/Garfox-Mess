#!/bin/bash

# log () {
#     clear
# }

log_loader () {
    
    log_load=$(cat ./log/s.json)

    if [ -z "$log_load" ]
    then
        echo "Create Log"
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

log_loader