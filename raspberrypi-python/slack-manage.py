import os

from slackclient import SlackClient

slack_token = 'xoxp-393473516853-392784516193-392646474624-70cbc54843a64c43cd31bfc52fb5ed22'
sc = SlackClient(slack_token)

# Get the data from the user
message = input("Get the data : ")
channel = 'python-projects'
call_type = "chat.postMessage"

for i in range(int(input("counter"))):
  sc.api_call(
    call_type,
    channel=channel,
    text=message
  )