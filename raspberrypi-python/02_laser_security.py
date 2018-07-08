from slackclient import SlackClient
import RPi.GPIO as gpio
import time


gpio.setmode(gpio.BOARD)

laser = 38
pres = 40

gpio.setup(laser, gpio.OUT)
gpio.setup(pres, gpio.IN)

# Slack Client configuration
slack_token = 'xoxp-393473516853-392784516193-392646474624-70cbc54843a64c43cd31bfc52fb5ed22'
sc = SlackClient(slack_token)

# Configure slack message
message = ""
channel = 'python-projects'
call_type = "chat.postMessage"

while True:
    gpio.output(laser, 0)
    time.sleep(1)
    message = ("Photo level in room is : ",gpio.input(pres))
    sc.api_call(call_type, channel=channel, text=message)

