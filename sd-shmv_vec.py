#!/usr/bin/env python2.7

# sd-shmv_vec.py
#
# Shutdown script BrewVectrex by MatixVision v1.0 - 2024
# www.matixvision.it
#
# GNU General Public License version 3
# https://www.gnu.org/licenses/gpl-3.0.en.html
#
#   /boot/config.txt
#  | #Uncomment some or all of these to enable the optional hardware interfaces
#  | #dtparam=i2c_arm=on
#  | #dtparam=i2s=on
# > | dtparam=spi=on
#  |
#  | #Uncomment this to enable infrared communication.
#  | #dtoverlay=gpio-ir,gpio_pin=17
#  | #dtoverlay=gpio-ir-tx,gpio_pin=18
#  |
#  | #Additional overlays and parameters are documented /boot/overlays/README
#  >| dtoverlay=gpio-shutdown, active_low, gpiopin=6
#  >| gpio=6=op,dl,pn
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
time.sleep(20)

ButtonONOFF = 0

while True: #loop
  inputgpio = GPIO.input(switchPin)
  if (ButtonONOFF == inputgpio ):
     os.system("sudo shutdown -h now")
     time.sleep(0.06)





