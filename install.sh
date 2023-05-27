#!/bin/bash

now=$(date +"%Y-%m-%d %H:%M:%S")
hostname=$(hostname)
os=$(uname)

data=$(cat <<EOF
{
    "name": "Garfox-mess",
    "version": "0.0.1",
    "production-date": "2023-05-26",
    "last-update": "$now",
    "system": {
        "OS": "$os",
        "host": "$hostname"
    }
}
EOF
)

echo "$data" > ./log/install.json

installation () {
    echo "Installing python3-pip..."
    apt-get install -y python3-pip

    echo "Installing python3..."
    apt-get install -y python3

    echo "Installing required packages..."
    pip3 install -r requirements.txt

    echo "Copying Garfox-mess to /opt..."
    cp -r ./Garfox-mess /opt/Garfox-mess

    echo "Creating symlink..."
    ln -s /opt/Garfox-mess/GM.py /usr/local/bin/myapp

    echo "Starting Garfox-mess..."
    python3 /opt/Garfox-mess/GM.py

    echo "Installation completed."
}

if [ -f ./log/log.json ]; then
    log_load=$(cat ./log/log.json)
   if [[ -z "$log_load" ]]; then
        echo "Log file not found. Creating new log file."
        installation
    else
        read -p "Log file found. You have already installed. Do you want to install again? [y/N]" answer
        if [[ "$answer" =~ ^[Yy]$ ]]; then
            echo "$data" > ./log/install.json
            installation
        else
            echo "Install Done"
            exit
        fi
    fi
else
    echo "Log file not found. Creating new log file."
    installation
fi

echo "$data" > ./log/log.json

