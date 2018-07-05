
import RPi.GPIO as gpio
import time


gpio.setmode(gpio.BOARD)

laser = 38

gpio.setup(led, gpio.OUT)

while True:
    gpio.output(laser, 1)
    time.sleep(1)
    gpio.output(laser, 0)
    time.sleep(0)