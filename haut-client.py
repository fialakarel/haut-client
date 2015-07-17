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

net = Network(CLIENT_LISTEN_IP, CLIENT_LISTEN_PORT)


net.send('{"hook": "login"}', "main.haut.local", 5556)

try:
    while True:
        # receive data
        data = net.recv()
        
        # wrong data, try it again
        if data == False:
            continue
        
        # variable HACK -- safe check
        try:
            cmd = data["cmd"]
        except TypeError:
            print("CMD NOT FOUND")
            continue
        except KeyError:
            print("CMD NOT FOUND")
            continue
        
        # variable HACK -- safe check
        try:
            arg = data["arg"]
        except KeyError:
            arg = ""
        
        # safe run
        print(data)
        os.system("./mod/" + cmd + " " + arg + " &")

except KeyboardInterrupt:
    net.send('{"hook": "logout"}', "main.haut.local", 5556)
    sys.exit(0)

net.send('{"hook": "failure"}', "main.haut.local", 5556)
