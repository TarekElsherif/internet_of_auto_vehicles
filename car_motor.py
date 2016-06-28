import RPi.GPIO as GPIO
import time
import sys
import Tkinter as tk
from pubnub import Pubnub
import json
import os

##pubnub = Pubnub(publish_key='pub-c-ac29425d-1f00-4df7-b227-24ed64baad79',
##                subscribe_key='sub-c-8a4aa916-1bc7-11e6-bfbc-02ee2ddab7fe')
##
##channel = 'home'
##
##os.chdir('./arm/bin')

# Enable GPIO pins DECLERATION (H-Bridge 1)
H1_enable_a = 23
H1_enable_b = 24

# Enable GPIO pins DECLERATION (H-Bridge 2)
H2_enable_a = 13
H2_enable_b = 19

# IN(1-4) GPIO pins DECLERATION (H-Bridge 1)
H1_IN1 = 4
H1_IN2 = 17
H1_IN3 = 27
H1_IN4 = 22

# IN(1-4) GPIO pins DECLERATION (H-Bridge 2)
H2_IN1 = 5
H2_IN2 = 6
H2_IN3 = 12
H2_IN4 = 16

def init():
    GPIO.setmode (GPIO.BCM)
    GPIO.setwarnings(False)

    # Enable GPIO pins SETUP (H-Bridge 1)
    GPIO.setup(H1_enable_a,GPIO.OUT)
    GPIO.setup(H1_enable_b,GPIO.OUT)

    # Enable GPIO pins SETUP (H-Bridge 2)
    GPIO.setup(H2_enable_a,GPIO.OUT)
    GPIO.setup(H2_enable_b,GPIO.OUT)

    # IN(1-4) GPIO pins SETUP (H-Bridge 1)
    GPIO.setup(H1_IN1,GPIO.OUT)
    GPIO.setup(H1_IN2,GPIO.OUT)
    GPIO.setup(H1_IN3,GPIO.OUT)
    GPIO.setup(H1_IN4,GPIO.OUT)

    # IN(1-4) GPIO pins SETUP (H-Bridge 2)
    GPIO.setup(H2_IN1,GPIO.OUT)
    GPIO.setup(H2_IN2,GPIO.OUT)
    GPIO.setup(H2_IN3,GPIO.OUT)
    GPIO.setup(H2_IN4,GPIO.OUT)

#///////////////////////////////////////////////////////////////////////////////
def stop():
    GPIO.cleanup()
    init()
    # Enable GPIO pins OUTPUT (H-Bridge 1)
    GPIO.output(H1_enable_a,False)
    GPIO.output(H1_enable_b,False)

    # Enable GPIO pins OUTPUT (H-Bridge 2)
    GPIO.output(H2_enable_a,False)
    GPIO.output(H2_enable_b,False)


def forward(tf):
##    GPIO.cleanup()
    init()
    # Enable GPIO pins OUTPUT (H-Bridge 1)
    GPIO.output(H1_enable_a,True)
    GPIO.output(H1_enable_b,True)

    # Enable GPIO pins OUTPUT (H-Bridge 2)
    GPIO.output(H2_enable_a,True)
    GPIO.output(H2_enable_b,True)

    # IN(1-4) GPIO pins OUTPUT (H-Bridge 1)
    GPIO.output(H1_IN1,True)
    GPIO.output(H1_IN2,False)
    GPIO.output(H1_IN3,True)
    GPIO.output(H1_IN4,False)

    # IN(1-4) GPIO pins OUTPUT (H-Bridge 2)
    GPIO.output(H2_IN1,True)
    GPIO.output(H2_IN2,False)
    GPIO.output(H2_IN3,True)
    GPIO.output(H2_IN4,False)
    time.sleep(tf)
    

def reverse(tf):
    GPIO.cleanup()
    init()
    # Enable GPIO pins OUTPUT (H-Bridge 1)
    GPIO.output(H1_enable_a,True)
    GPIO.output(H1_enable_b,True)

    # Enable GPIO pins OUTPUT (H-Bridge 2)
    GPIO.output(H2_enable_a,True)
    GPIO.output(H2_enable_b,True)

    # IN(1-4) GPIO pins OUTPUT (H-Bridge 1)
    GPIO.output(H1_IN1,False)
    GPIO.output(H1_IN2,True)
    GPIO.output(H1_IN3,False)
    GPIO.output(H1_IN4,True)

    # IN(1-4) GPIO pins OUTPUT (H-Bridge 2)
    GPIO.output(H2_IN1,False)
    GPIO.output(H2_IN2,True)
    GPIO.output(H2_IN3,False)
    GPIO.output(H2_IN4,True)
    time.sleep(tf)


def turn_right(tf):
    GPIO.cleanup()
    init()
    # Enable GPIO pins OUTPUT (H-Bridge 1)
    GPIO.output(H1_enable_a,True)
    GPIO.output(H1_enable_b,True)

    # Enable GPIO pins OUTPUT (H-Bridge 2)
    GPIO.output(H2_enable_a,False)
    GPIO.output(H2_enable_b,False)

    # IN(1-4) GPIO pins OUTPUT (H-Bridge 1)
    GPIO.output(H1_IN1,True)
    GPIO.output(H1_IN2,False)
    GPIO.output(H1_IN3,True)
    GPIO.output(H1_IN4,False)
    time.sleep(tf)

def turn_left(tf):
    GPIO.cleanup()
    init()
    # Enable GPIO pins OUTPUT (H-Bridge 1)
    GPIO.output(H1_enable_a,False)
    GPIO.output(H1_enable_b,False)

    # Enable GPIO pins OUTPUT (H-Bridge 2)
    GPIO.output(H2_enable_a,True)
    GPIO.output(H2_enable_b,True)

    # IN(1-4) GPIO pins OUTPUT (H-Bridge 2)
    GPIO.output(H2_IN1,True)
    GPIO.output(H2_IN2,False)
    GPIO.output(H2_IN3,True)
    GPIO.output(H2_IN4,False)
    time.sleep(tf)


def pivot_right(tf):
    GPIO.cleanup()
    init()
    # Enable GPIO pins OUTPUT (H-Bridge 1)
    GPIO.output(H1_enable_a,True)
    GPIO.output(H1_enable_b,True)

    # Enable GPIO pins OUTPUT (H-Bridge 2)
    GPIO.output(H2_enable_a,True)
    GPIO.output(H2_enable_b,True)

    # IN(1-4) GPIO pins OUTPUT (H-Bridge 1)
    GPIO.output(H1_IN1,True)
    GPIO.output(H1_IN2,False)
    GPIO.output(H1_IN3,True)
    GPIO.output(H1_IN4,False)

    # IN(1-4) GPIO pins OUTPUT (H-Bridge 2)
    GPIO.output(H2_IN1,False)
    GPIO.output(H2_IN2,True)
    GPIO.output(H2_IN3,False)
    GPIO.output(H2_IN4,True)
    time.sleep(tf)

def pivot_left(tf):
    GPIO.cleanup()
    init()
    # Enable GPIO pins OUTPUT (H-Bridge 1)
    GPIO.output(H1_enable_a,True)
    GPIO.output(H1_enable_b,True)

    # Enable GPIO pins OUTPUT (H-Bridge 2)
    GPIO.output(H2_enable_a,True)
    GPIO.output(H2_enable_b,True)

    # IN(1-4) GPIO pins OUTPUT (H-Bridge 1)
    GPIO.output(H1_IN1,False)
    GPIO.output(H1_IN2,True)
    GPIO.output(H1_IN3,False)
    GPIO.output(H1_IN4,True)

    # IN(1-4) GPIO pins OUTPUT (H-Bridge 2)
    GPIO.output(H2_IN1,True)
    GPIO.output(H2_IN2,False)
    GPIO.output(H2_IN3,True)
    GPIO.output(H2_IN4,False)
    time.sleep(tf)

stop()
