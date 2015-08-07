#!/usr/bin/python2

# author: Karel Fiala
# email: fiala.karel@gmail.com

# version: 0.1.0

import os, sys

pin = sys.argv[1]
val = sys.argv[2]
    
os.system("echo " + str(pin) + "=" + str(val) + ">/dev/pi-blaster")