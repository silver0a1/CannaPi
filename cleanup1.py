#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import sys
GPIO.setmode(GPIO.BCM)
PWR = 4
GPIO.setwarnings(False)
GPIO.setup(PWR, GPIO.OUT)
GPIO.output(PWR, False)
GPIO.cleanup()
