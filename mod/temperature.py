#!/usr/bin/python

# author: Karel Fiala
# email: fiala.karel@gmail.com

# version: 0.2.0

import sys, os
import time
from network import Network
from config import *

net = Network()

temp_sensor = "/sys/bus/w1/devices/" + str(sys.argv[1]) + "/w1_slave"

def temp_raw():
    f = open(temp_sensor, 'r')
    lines = f.readlines()
    f.close()
    return lines

lines = temp_raw()
while lines[0].strip()[-3:] != 'YES':
    time.sleep(0.2)
    lines = temp_raw()

temp_output = lines[1].find('t=')

if temp_output != -1:
    temp_string = lines[1].strip()[temp_output+2:]
    temp_c = float(temp_string) / 1000.0


data = dict()
data["key"] = str(sys.argv[1])
data["value"] = temp_c
net.send(data, "main.haut.local" , SERVER_PORT)
