#!/bin/bash


log () {

    now=$(date +"%Y-%m-%d %H:%M:%S")
    hostname=$(hostname)
    os=$(uname)

    from=$(cat <<EOF
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

    echo "$from" > ./log/install.json
    
}

log_loader () {
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
    log_load=$(cat ./log/log.json)

    if [ -z "$log_load" ]
    then
        echo "Log file not found. Creating new log file."
	installation
    else
        echo "Log file found."
    fi
}

log_loader
log
