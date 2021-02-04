# Globals
from dotenv import load_dotenv
load_dotenv()
import os
from servicebus.servicebus import receive_messages

# Methods

# Main program
print("IFIDUK Server Agent Version 1.0")
print("Waiting for messages...")
receive_messages()

