# Globals
from dotenv import load_dotenv
load_dotenv()
import os
from servicebus.servicebus import receive_messages
import json

# Methods

# Main program
print("\nIFIDUK Server Agent Version 1.0\n")

while True:
    print("Waiting for messages...")
    raw_message = receive_messages()
    message = json.loads(raw_message)
    subscription_id = message["_id"]
    product_id = message["productId"]
    print("Processing subscription:")
    print("Subscription ID: " + subscription_id)
    print("Product ID: " + product_id)
    print("\n")
