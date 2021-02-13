# Globals
from dotenv import load_dotenv
load_dotenv()
import os
from servicebus.servicebus import receive_messages, send_message
import json
from deploy.manage_tenant import create_tenant, delete_tenant 
from deploy.manage_dns import create_dns, delete_dns

# Methods
def action_create(message):
    subscription_id = message["subscriptionId"]
    name = message["name"]

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

    # Add virtual host env variables
    virtual_host = message["name"] + ".onifiduk.com"
    fe_env.append("VIRTUAL_HOST=" + virtual_host)
    fe_env.append("LETSENCRYPT_HOST=" + virtual_host)

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
    create_tenant(subscription_id, fe_image, fe_name, fe_env, be_image, be_name, be_env)

    # Create DNS record
    create_dns(name)

    # Send confirmation
    confirmation = {
            "status": "Running",
            "subscriptionId": subscription_id
    }

    confirmation_json = json.dumps(confirmation)

    send_message(confirmation_json)

def action_delete(message):
    subscription_id = message["subscriptionId"]
    name = message["name"]

    # Get frontend config
    fe_name = subscription_id + "_fe"
    print("Front End Config:")
    print("Name: " + fe_name)
    
    print("\n")

    # Get backend config
    be_name = subscription_id + "_be"
    print("Back End Config:")
    print("Name: " + be_name)
    
    # Delete containers
    delete_tenant(subscription_id, fe_name, be_name)

    # Create DNS record
    delete_dns(name)

    # Send confirmation
    confirmation = {
            "status": "Deleted",
            "subscriptionId": subscription_id
    }

    confirmation_json = json.dumps(confirmation)

    send_message(confirmation_json)


# Main program
print("\nIFIDUK Server Agent Version 1.0\n")

while True:
    print("Waiting for messages...")
    
    raw_message = receive_messages()
    message = json.loads(raw_message)
    subscription_id = message["subscriptionId"]
    name = message["name"]
    action = message["action"]
    
    print("Processing subscription:")
    
    #print(message)
    print("Action: " + action)
    print("Subscription ID: " + subscription_id)
    print("Subscription Name: " + name)
    print("\n")
    
    if action == "create":
        action_create(message)
    elif action == "delete":
        action_delete(message)
    

    
