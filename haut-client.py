#!/usr/bin/python3

# author: Karel Fiala
# email: fiala.karel@gmail.com

# version 0.2

"""
hlavni smycka klienta pro spousteni modulu
"""

import os, sys
from network import Network
from datetime import datetime
from modules import *
from config import *
import threading

net = Network(CLIENT_IP, CLIENT_PORT)

net.send({"key": "status", "value": "login"}, SERVER_IP, SERVER_PORT)

try:
    while True:

        x = ""
        # receive data
        data = net.recv()

        # wrong data, try it again
        if data == False:
            continue

        # variable HACK -- safe check
        try:
            cmd = data["cmd"]
        except TypeError:
            x = x + "CMD NOT FOUND"
            continue
        except KeyError:
            x = x + "CMD NOT FOUND"
            continue

        # variable HACK -- safe check
        try:
            arg = tuple(data["arg"].split(' '))
        except KeyError:
            arg = ""

        # safe run
        print(str(datetime.now()) + " " + str(data) + " " + str(x))
        #os.system("./mod/" + cmd + " " + arg + " &")
        if arg[0] == '':
            (threading.Thread(target=eval(cmd))).start()
        else:
            (threading.Thread(target=eval(cmd), args=arg )).start()

except KeyboardInterrupt:
    net.send({"key": "status", "value": "logout"}, SERVER_IP, SERVER_PORT)
    os.system('( sleep 2 ; for x in `pidof python3` ; do sudo kill -9 $x ; done ) &')
    sys.exit(0)

net.send({"key": "status", "value": "failure"}, SERVER_IP, SERVER_PORT)
