#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import commands

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(27, GPIO.IN)
GPIO.setup(22, GPIO.OUT, initial=GPIO.HIGH)

try:
    while True:
        GPIO.wait_for_edge(27, GPIO.FALLING)
        time.sleep(1)
        if GPIO.input(27) == 1:
            #GPIO.output(22, GPIO.LOW)
            commands.getoutput("shutdown -h now")
except KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()
