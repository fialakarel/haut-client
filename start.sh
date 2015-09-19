#!/bin/bash

# author: Karel Fiala
# email: fiala.karel@gmail.com

# wait for boot
sleep 10 ;

# logs
log="/root/haut-client-start.log"
printf "\n\n===== `date` =====\n" >>$log

# go to 
cd /root/haut-client

# update client
git pull &>>$log

# run client in screen
( screen -S 'haut-client' -d -m ./haut-client.py ) &

exit 0


