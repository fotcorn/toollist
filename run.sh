#!/bin/bash
cd ~/toollist
source ~/toollist_venv/bin/activate
git pull origin master
./manage.py migrate toollist
cd toollist
../manage.py compilemessages
cd ..
./manage.py runserver 0.0.0.0:54321

