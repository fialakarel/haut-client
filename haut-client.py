#!/usr/bin/python3

# author: Karel Fiala
# email: fiala.karel@gmail.com

# version 0.2

"""
hlavni smycka klienta pro spousteni modulu
"""

import os, sys
from mod.network import Network
from mod.config import *
from datetime import datetime

net = Network(CLIENT_LISTEN_IP, CLIENT_LISTEN_PORT)


net.send('{"key": "hook", "value": "login"}', "main.haut.local", 5556)

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
        os.system("./mod/" + cmd + " " + arg + " &")

except KeyboardInterrupt:
    net.send('{"key": "hook", "value": "logout"}', "main.haut.local", 5556)
    sys.exit(0)

net.send('{"key": "hook", "value": "failure"}', "main.haut.local", 5556)
