#!/bin/bash

# wait for boot
sleep 10 ;

# clear log
log="/home/pi/haut-client-start.log"
>$log

# go to 
cd /home/pi/haut-client

# update client
git pull &>>$log

# run client in screen
( screen -S 'haut-client' -d -m ./haut-client.py ) &

exit 0


