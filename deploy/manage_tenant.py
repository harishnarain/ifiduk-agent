# Imports
import docker

# Globals
client = docker.from_env()

# Methods

def create_tenant(subscription_id, fe_image, fe_name, fe_env, be_image, be_name, be_env):
    print("Deploying subscription: " + subscription_id)

    # Create network
    network = subscription_id + "_net"
    print("Creating network: " + network)
    client.networks.create(network, driver="bridge", attachable=True, internal=True)
    network_object = client.networks.get(network)

    # Create front end
    print("Starting container: " + fe_name)
    client.containers.run(fe_image, detach=True, name=fe_name, network="bridge", environment=fe_env)
    network_object.connect(fe_name)

    # Create back end
    print("Starting container: " + be_name)
    client.containers.run(be_image, detach=True, name=be_name, network=network, environment=be_env)

def delete_tenant(subscription_id, fe_name, be_name):
    print("Deleting tenant: " + subscription_id)

    # Create objects for fe and be containers
    fe_container = client.containers.get(fe_name)
    be_container = client.containers.get(be_name)

    # Stop front end
    print("Stopping container: " + fe_name)
    fe_container.stop()

    # Delete front end
    print("Deleting container: " + fe_name)
    fe_container.remove()

    # Stop back end
    print("Stopping container: " + be_name)
    be_container.stop()

    # Delete back end
    print("Deleting container: " + be_name)
    be_container.remove()

    # Delete network
    network = subscription_id + "_net"
    print("Deleting network: " + network)
    network_object = client.networks.get(network)
    network_object.remove()

