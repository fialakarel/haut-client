#!/usr/bin/python3

# author: Karel Fiala
# email: fiala.karel@gmail.com

# version 0.1.0
"""
class xxx(object):

    def __init__(self):
        pass
"""
import sys, os
import time
from network import Network
import RPi.GPIO as io

# settings
io.setmode(io.BCM)

net = Network()
SERVER_PORT = 5556

mem = dict()

def status():
    data = dict()
    data["key"] = "status"
    data["value"] = os.popen("uptime").read()
    net.send(data, "main.haut.local" , SERVER_PORT)

    
def fade(pin, fro, to, step=2, sleep=0.05):
    pin=int(pin)
    fro=float(fro)
    to=float(to)
    step=float(step)
    sleep=float(sleep)
    
    if fro > to and step > 0:
        step = step * -1
    
    for x in range(int(fro*100), int(to*100), int(step)):
        os.system("echo " + str(pin) + "=" + str(float(x)/100) + ">/dev/pi-blaster")
        time.sleep(sleep)
    time.sleep(sleep)
    os.system("echo " + str(pin) + "=" + str(to) + ">/dev/pi-blaster")

    
def blaster(pin, val):
    os.system("echo " + str(pin) + "=" + str(val) + ">/dev/pi-blaster")


# true / false
def gpio(pin, val):
    io.setup(pin, io.OUT)         # activate input
    io.output(pin, val)


def temperature(temp_id):
    temp_sensor = "/sys/bus/w1/devices/" + temp_id + "/w1_slave"

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
    data["key"] = temp_id
    data["value"] = temp_c
    net.send(data, "main.haut.local" , SERVER_PORT)


def pir(pin):
    global mem
    
    try:
        if mem["pir"][pin]:
            return
    except KeyError:
        pass
    
    try:
        mem["pir"][pin] = True
    except KeyError:
        mem["pir"] = dict()
        mem["pir"][pin] = True        
    
    pir_pin = int(pin)
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
        
        time.sleep(0.05)
