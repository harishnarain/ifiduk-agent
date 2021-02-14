# IFIDUK - The marketplace for web based apps

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

IFIDUK is an app suite for running your own SaaS marketplace. You assemble your app and deploy it on IFIDUK where your users can visit and deploy their own instances.

The suite consists of the following:

- A ReactJS front end that uses Azure Active Directory B2C for authentication and authorization - https://github.com/harishnarain/ifiduk-app
- An Azure Functions App that handles all CRUD operations and a MongoDB seeder. The functions app will also require Azure Service Bus for sending deployment messages - https://github.com/harishnarain/ifiduk-deployment-function
- The IFIDUK Server Agent that deploys containers on Docker - https://github.com/harishnarain/ifiduk-agent
- IFIDUK Terraform code to deploy services on Azure (Work in progress) - https://github.com/harishnarain/ifiduk-terraform

## Table of Contents

- [IFIDUK - The marketplace for web based apps](#ifiduk---the-marketplace-for-web-based-apps)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Routes](#routes)
  - [Features](#features)
  - [License](#license)
  - [Contributing](#contributing)
  - [Screenshots](#screenshots)
  - [Questions](#questions)

## Installation

This is the installation instructions for the IFIDUK Server Agent.

1. Clone this GitHub repository

   ```
   git@github.com:harishnarain/ifiduk-agent.git
   ```

2. Install all dependent pip packages

   ```
   pip3 install docker
   pip3 install azure.core
   pip3 install azure-mgmt-dns
   pip3 install azure.common
   pip3 install python-dotenv
   pip3 install azure-servicebus
   ```

3. Create a user in Azure AD that has roles scoped to manage DNS records

4. Create a .env file and populate the following environment variables
   SERVICEBUS_CONNECTION_STRING="Enter your Azure Service Bus connection string"
   SERVICEBUS_QUEUE_NAME="deployment"
   SERVICEBUS_QUEUE_NAME="deployment"
   SERVICEBUS_SEND_QUEUE="post-deployment"
   SUBSCRIPTION_ID="Enter your Azure subscription ID"
   AAD_DNS_USER="Enter the UPN of the user account you created in step 3"
   AAD_DNS_PWD="Enter the password for the user account you created in step 3"

5. Install the Docker engine

6. Run the IFIDUK server agent by running python3 ifiduk-agent.py (This hasn't been daemonized. This is still under development)

## Deployment or Deletion process

1. The agent will pick up the request from the Azure Service Bus queue
2. Create a network for the front end and backend containers to communicate
3. Create containers for front end and backend services
4. Create DNS record for the tenant in Azure DNS
5. Create a post deployment JSON message and sends it to the Azure Service Bus post deployment queue to be processed by the IFIDUK deployment API Azure Function App

## Features

- Python 3
- Azure Service Bus SDK
- Azure SDK for DNS
- Docker SDK
- Python-Dotenv

## License

This project uses the MIT license

## Contributing

Pull requests are welcome

## Screenshots

![Screenshot4](https://github.com/harishnarain/ifiduk-agent/blob/main/Screenshot4.png?raw=true)

## Questions

Checkout my GitHub [profile](https://github.com/harishnarain)

Please feel free to email at: <Harish.Narain@microsoft.com>
