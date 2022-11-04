#! /bin/bash

echo 'Gunicorn Running Directory'
echo $PWD

echo 'User'
echo "$USER"

sudo systemctl daemon-reload
sudo systemctl start gunicorn

echo "Gunicorn has started."

sudo systemctl enable gunicorn

echo "Gunicorn has been enabled."

sudo systemctl restart gunicorn

sudo systemctl status gunicorn

