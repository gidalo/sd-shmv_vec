#!/usr/bin/env python2.7

# sd-shmv_vec.py
#
# Shutdown script BrewVectrex by MatixVision v1.0 - 2024
# www.matixvision.it
#
# GNU General Public License version 3
# https://www.gnu.org/licenses/gpl-3.0.en.html
#

import os
import time
import RPi.GPIO as GPIO

from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# switchPin 6 = GPIO6 (PIN 31 HW)
switchPin = 6

GPIO.setup(switchPin, GPIO.IN)
GPIO.input(switchPin)
while True:
  input = GPIO.input(switchPin)
  if (input == 1):
    os.system("sudo shutdown -h now")
    time.sleep(0.06)
