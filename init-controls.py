#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

# for 1st Motor on ENA
ENA = 19
IN1 = 23
IN2 = 21

ENB = 22
IN3 = 24
IN4 = 26

# set pin numbers to the board's
GPIO.setmode(GPIO.BOARD)

# initialize EnA, In1 and In2
GPIO.setup(ENA, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(ENB, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)

# Stop
GPIO.output(ENA, GPIO.HIGH)
GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.LOW)

GPIO.output(ENB, GPIO.HIGH)
GPIO.output(IN3, GPIO.LOW)
GPIO.output(IN4, GPIO.LOW)
time.sleep(1)

# Forward
GPIO.output(IN1, GPIO.HIGH)
GPIO.output(IN2, GPIO.LOW)

GPIO.output(IN3, GPIO.HIGH)
GPIO.output(IN4, GPIO.LOW)
time.sleep(1)

# Stop
GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.LOW)

GPIO.output(IN3, GPIO.LOW)
GPIO.output(IN4, GPIO.LOW)
time.sleep(1)

# Backward
GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.HIGH)

GPIO.output(IN3, GPIO.LOW)
GPIO.output(IN4, GPIO.HIGH)
time.sleep(1)

# Stop
GPIO.output(ENA, GPIO.LOW)
GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.LOW)

GPIO.output(ENB, GPIO.LOW)
GPIO.output(IN3, GPIO.LOW)
GPIO.output(IN4, GPIO.LOW)
time.sleep(1)

GPIO.cleanup()
