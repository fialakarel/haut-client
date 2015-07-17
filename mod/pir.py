#!/usr/bin/python3

# author: Karel Fiala
# email: fiala.karel@gmail.com

# version: 0.2.0

import sys, os
import time
from network import Network
from config import *
import RPi.GPIO as io

processname = './mod/pir.py'
tmp = os.popen("ps -aux").read()
proccount = tmp.count(processname)

if proccount > 0:
    print("PIR already running -> exiting")
    sys.exit(1)

net = Network()

io.setmode(io.BCM)
pir_pin = int(sys.argv[1])
io.setup(pir_pin, io.IN)         # activate input

data = dict()
data["key"] = "pir-" + str(pir_pin)

state = io.input(pir_pin)
data["value"] = state
net.send(data, "main.haut.local" , SERVER_PORT)
 
while True:
    if io.input(pir_pin) != state:
        if state == 0:
            state = 1
            data["value"] = state
            net.send(data, "main.haut.local" , SERVER_PORT)
        else:
            state = 0
            data["value"] = state
            net.send(data, "main.haut.local" , SERVER_PORT)
    
    time.sleep(0.1)
