#!/bin/bash

declare -A users=(
    ["user1"]="pass1"
    ["user2"]="pass2"
)

handle_client() {
    while true; do
        message=$(echo "$1" | tr -d '\r' | nc -l -p 8000)
        if [ ! -z "$message" ]; then
            parts=(${message//:/ })
            username="${parts[0]}"
            password="${parts[1]}"

            if [[ ${users[$username]} == $password ]]; then
                echo "User $username connected."
            else
                echo "User $username failed to connect."
            fi
        fi
    done
}

start_server() {
    echo "Server started."
    while true; do
        client_socket=$(nc -l -p 8000)
        client_thread=$(handle_client "$client_socket" &)
    done
}

start_client() {
    read -p "Enter server IP address: " server_ip
    server_port=8000

    echo "Connected to server."
    read -p "Enter username: " username
    read -p "Enter password: " password

    credentials="$username:$password"
    echo "$credentials" | nc $server_ip $server_port
}

main() {
    read -p "Choose 's' for server or 'c' for client: " choice

    if [[ $choice == "s" ]]; then
        start_server
    elif [[ $choice == "c" ]]; then
        start_client
    else
        echo "Invalid choice."
    fi
}

main
