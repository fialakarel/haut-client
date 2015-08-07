#!/usr/bin/python2

# author: Karel Fiala
# email: fiala.karel@gmail.com

# version: 0.1.0

import os, time, sys

pin = int(sys.argv[1])
to = float(sys.argv[2])

for x in range(0, int(to*100), 3):
    os.system("echo " + str(pin) + "=" + str(float(x)/100) + ">/dev/pi-blaster")
    time.sleep(0.1)
    
os.system("echo " + str(pin) + "=" + str(to) + ">/dev/pi-blaster")