#! /bin/bash

echo 'Gunicorn Running Directory'
echo $PWD

echo 'User'
echo "$USER"

sudo systemctl daemon-reload
sudo systemctl start media_manager

echo "Gunicorn has started."

sudo systemctl enable media_manager

echo "Gunicorn has been enabled."

sudo systemctl restart media_manager

sudo systemctl status media_manager

