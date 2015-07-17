#!/usr/bin/python2

# author: Karel Fiala
# email: fiala.karel@gmail.com

# version: 0.2.0

import sys
import RPi.GPIO as io
io.setmode(io.BCM)
 
led_pin = int(sys.argv[1])
io.setup(led_pin, io.OUT)         # activate input

if int(sys.argv[2]):
    io.output(led_pin, True)
else:
    io.output(led_pin, False)

