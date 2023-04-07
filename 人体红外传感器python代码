import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

makerobo_pirPin = 17
makerobo_redPin = 18
makerobo_greenPin = 27
makerobo_bluePin = 22

GPIO.setup(makerobo_pirPin, GPIO.IN)
GPIO.setup(makerobo_redPin, GPIO.OUT)
GPIO.setup(makerobo_greenPin, GPIO.OUT)
GPIO.setup(makerobo_bluePin, GPIO.OUT)

red = GPIO.PWM(makerobo_redPin, 100)
green = GPIO.PWM(makerobo_greenPin, 100)
blue = GPIO.PWM(makerobo_bluePin, 100)

def makerobo_ledInit():
    red.start(0)
    green.start(0)
    blue.start(0)

def makerobo_ledColorSet(r_val, g_val, b_val):
    red.ChangeDutyCycle(r_val)
    green.ChangeDutyCycle(g_val)
    blue.ChangeDutyCycle(b_val)

try:
    makerobo_ledInit()
    while True:
        makerobo_pir_val = GPIO.input(makerobo_pirPin)
        if makerobo_pir_val == 1:
            makerobo_ledColorSet(100, 100, 0)
        else:
            makerobo_ledColorSet(0, 0, 100)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
