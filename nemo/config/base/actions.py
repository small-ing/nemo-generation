from nemoguardrails.actions import action
import random

@action()
async def random():
    print("Random action called")
    return random.randint(1000, 1500)

@action()
async def print_log():
    print("Print log action called")
    return "Print log action called"