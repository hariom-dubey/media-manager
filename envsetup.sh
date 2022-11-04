#!/bin/bash

echo 'ENV Setup Running Directory'
echo $PWD

if [ -d 'django_env' ]
then
   echo 'Python virtual environment exists'
else
    python3 -m venv django_env
fi

source django_env/bin/activate

pip install -r requirements.txt

if [ -d 'logs' ]
then
   echo 'Log folder exists'
else
    mkdir logs
    touch logs/error.log logs/access.log
fi

sudo chmod -R 777 logs

echo 'ENV Setup Finished'