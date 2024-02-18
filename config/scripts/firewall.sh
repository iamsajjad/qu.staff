#!/bin/bash

if [[ $UID != 0 ]]; then
    echo "Error: Permission required to configure"
    echo "sudo bash $0"
    exit 1
fi

# allow 8000, 80, 443 ports in firewall
echo "Port 8000 allowed"
ufw allow 8000/tcp

echo "Port 80 allowed"
ufw allow 80/tcp

echo "Port 443 allowed"
ufw allow 443/tcp
