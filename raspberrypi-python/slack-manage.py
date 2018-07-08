

from slackclient import SlackClient

slack_token = 'xoxp-393473516853-392784516193-392698899968-0d5405a8e6494dfca7de6835981b447a'
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