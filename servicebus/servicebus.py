# Imports
from dotenv import load_dotenv
from azure.servicebus import ServiceBusClient, ServiceBusMessage
load_dotenv()
import os

# Globals
SERVICEBUS_CONNECTION_STRING = os.getenv("SERVICEBUS_CONNECTION_STRING")
SERVICEBUS_QUEUE_NAME = os.getenv("SERVICEBUS_QUEUE_NAME")
servicebus_client = ServiceBusClient.from_connection_string(conn_str=SERVICEBUS_CONNECTION_STRING, logging_enable=True)

# Methods

def receive_messages():
    with servicebus_client:
        receiver = servicebus_client.get_queue_receiver(queue_name=SERVICEBUS_QUEUE_NAME)
        with receiver:
            for msg in receiver:
                print("Received: " + str(msg))
                receiver.complete_message(msg)

