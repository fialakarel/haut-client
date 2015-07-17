#!/usr/bin/python3

# author: Karel Fiala
# email: fiala.karel@gmail.com

# version: 0.2.0

import sys, os
import time
from network import Network
from config import *

net = Network()

data = dict()
data["key"] = "status"
data["value"] = os.popen("uptime").read()

net.send(data, "main.haut.local" , SERVER_PORT)
