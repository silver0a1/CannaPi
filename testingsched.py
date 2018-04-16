#!/usr/bin/env python
import RPi.GPIO as GPIO
import sys
import time
from time import sleep
#sys.arg[1..2..3...etc] for parameters
PWR = 4 
TTP = float(900.0)
TTS = float(1800.0)

#RELAY

try:
    while True:
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(PWR, GPIO.OUT)
        GPIO.output(PWR, True)
        sleep(TTP)
	GPIO.output(PWR, False)
	GPIO.cleanup()
	sleep(TTS)
except KeyboardInterrupt, e:
    logging.info("Stopping...")



#
#print(TTP)
#time.sleep(TTP)
#print('Yeahh')
#exit()


