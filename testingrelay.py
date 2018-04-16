#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import sys
GPIO.setmode(GPIO.BCM)
PWR = 4
TTP = float(sys.argv[1])
GPIO.setwarnings(False)
GPIO.setup(PWR, GPIO.OUT)
GPIO.output(PWR, True)
time.sleep(TTP)
GPIO.output(PWR, False)
GPIO.cleanup()
