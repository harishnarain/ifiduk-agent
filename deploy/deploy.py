# Imports
import docker

# Globals
client = docker.from_env()

# Methods

def deploy_subscription(subscription_id, fe_image, fe_name, fe_env, be_image, be_name, be_env):
    print("Deploying subscription: " + subscription_id)

    # Create network
    network = subscription_id + "_net"
    print("Creating network: " + network)
    client.networks.create(network, driver="bridge")

    # Create front end
    print("Starting container: " + fe_name)
    client.containers.run(fe_image, detach=True, name=fe_name, network=network, ports={'80/tcp': 8080}, environment=be_env)

    # Create back end
    print("Starting container: " + be_name)
    client.containers.run(be_image, detach=True, name=be_name, network=network, environment=be_env)

