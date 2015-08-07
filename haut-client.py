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
import threading

net = Network("0.0.0.0", 5555)

SERVER_PORT = 5556

net.send({"key": "status", "value": "login"}, "main.haut.local", 5556)

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
            arg = data["arg"]
        except KeyError:
            arg = ""
        
        # safe run
        print(str(datetime.now()) + " " + str(data) + " " + str(x))
        #os.system("./mod/" + cmd + " " + arg + " &")
        (threading.Thread(target=cmd, args=(arg))).start()

except KeyboardInterrupt:
    net.send({"key": "status", "value": "logout"}, "main.haut.local", 5556)
    os.system('( sleep 2 ; for x in `pidof python3` ; do sudo kill -9 $x ; done ) &')
    sys.exit(0)

net.send({"key": "status", "value": "failure"}, "main.haut.local", 5556)
