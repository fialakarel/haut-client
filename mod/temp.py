#!/usr/bin/python3

# author: Karel Fiala
# email: fiala.karel@gmail.com

# version: 0.2.0

import sys, os
import time
from network import Network
from config import *
import random

# cteni argumentu
# print(len(sys.argv))

#for arg in sys.argv:
#    print(arg)


net = Network()

data = dict()
data["key"] = "temp1"
data["value"] = random.randint(20,30)
#print(sys.argv[0] + ": " + "funguju")

net.send(data, "main.haut.local", SERVER_PORT)
