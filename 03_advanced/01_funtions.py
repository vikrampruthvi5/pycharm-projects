"""

Lets learn function
Function is used for code re usability

"""


def beef():  # Function is defined with def keyword in the front
    print(name, "Welcome to Python coding")


def btc_to_usd(btc):
    amount = btc * 527
    print(btc, "Bit Coins values", amount, "$")


name = input("Enter your name : ")
beef()
btc_to_usd(float(input("Enter count of bit coins : ")))
