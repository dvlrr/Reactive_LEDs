from machine import Pin
from neopixel import Neopixel
import utime
import math

# define pins
trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

numpix = 15
pixels = Neopixel(numpix, 0, 28, "GRB")

yellow = (255, 100, 0)
orange = (255, 50, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

# Sensor loop

def ultra():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()

    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()

    timepassed = signalon - signaloff
    distancesum = (timepassed * 0.0343) / 2
    distance = math.trunc(distancesum)

    #print("Distance to sensor is ", distance, "cm")

    if distance < 100:
        return distance

    else:
        return 100

while True:

    prox = ultra()

    dimval = 100 - prox

    pixels.brightness(dimval)
    print(dimval)
    print(prox)
    pixels.fill(blue)
    pixels.show()

    utime.sleep(0.05)
