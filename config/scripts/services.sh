#!/bin/bash

if [[ $UID != 0 ]]; then
    echo "Error: Permission required to configure"
    echo "sudo bash $0"
    exit 1
fi

# copy gunicorn service file to `/etc/systemd/system/`
cp ./gunicorn.service /etc/systemd/system/

# copy caddy service file to `/etc/systemd/system/`
cp ./caddy.service /etc/systemd/system/

# reload `systemctl` daemon
systemctl daemon-reload

# start gunicorn service
systemctl restart gunicorn.service

# start caddy service
systemctl restart caddy.service

# enable gunicorn service
systemctl enable gunicorn.service

# enable gunicorn service
systemctl enable caddy.service
