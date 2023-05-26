#!/bin/bash

log () {

    now=$(date +"%Y-%m-%d %H:%M:%S")
    hostname=$(hostname)
    os=$(uname)

    fruom=$(cat <<EOF
    {
        "name":"Garfox-mess",
        "version":"0.0.1",
        "production-date":"2023-05-26",
        "last-update":"$now",
        "system" : {
            "OS":"$os",
            "host":"$hostname"
        }
    }
    EOF
    )

    echo "$fruom" > ./log/install.json
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