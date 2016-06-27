import RPi.GPIO as GPIO
import time
import sys
import os
import picamera

camera = picamera.PiCamera()
camera.start_preview()
time.sleep(10)
camera.stop_preview()
