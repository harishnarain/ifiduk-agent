# Globals
from dotenv import load_dotenv
load_dotenv()
import os
from servicebus.servicebus import receive_messages
import json
from deploy.deploy import deploy_subscription

# Methods

# Main program
print("\nIFIDUK Server Agent Version 1.0\n")

while True:
    print("Waiting for messages...")
    
    raw_message = receive_messages()
    message = json.loads(raw_message)
    subscription_id = message["subscriptionId"]
    name = message["name"]
    
    print("Processing subscription:")
    
    #print(message)
    
    print("Subscription ID: " + subscription_id)
    print("Subscription Name: " + name)
    print("\n")
    
    # Get frontend config
    fe_image = message["frontend"]["image"]
    fe_name = message["frontend"]["name"]
    fe_env = []
    print("Front End Config:")
    print("Name: " + message["frontend"]["name"])
    print("Image: " + message["frontend"]["image"])
    
    if (len(message["frontend"]["env"]) > 0):
        print("\nEnvironment variables:")
        for env in message["frontend"]["env"]:
            print(list(env)[0] + "=" + env[list(env)[0]])
            fe_env.append(list(env)[0] + "=" + env[list(env)[0]])
            
    print("\n")

    # Get backend config
    be_image = message["backend"]["image"]
    be_name = message["backend"]["name"]
    be_env = []
    print("Back End Config:")
    print("Name: " + message["backend"]["name"])
    print("Image: " + message["backend"]["image"])
    print("Port: " + str(message["backend"]["port"]))

    if (len(message["backend"]["env"]) > 0):
        print("\nEnvironment variables:")
        for env in message["backend"]["env"]:
            print(list(env)[0] + "=" + env[list(env)[0]])
            be_env.append(list(env)[0] + "=" + env[list(env)[0]])

    # Deploy containers
    deploy_subscription(subscription_id, fe_image, fe_name, fe_env, be_image, be_name, be_env)

