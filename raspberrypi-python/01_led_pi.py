
import RPi.GPIO as gpio
import time


gpio.setmode(gpio.BOARD)

led = 6

gpio.setup(led, gpio.OUT)

while True:
    gpio.output(led, 1)
    time.sleep(1)
    gpio.output(led, 0)
    time.sleep(0)