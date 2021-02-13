from azure.mgmt.dns import DnsManagementClient
from azure.common.credentials import UserPassCredentials
from dotenv import load_dotenv
load_dotenv()
import os

subscription_id = os.getenv("SUBSCRIPTION_ID")

AAD_USER = os.getenv("AAD_DNS_USER")
AAD_PWD = os.getenv("AAD_DNS_PWD")

credentials = UserPassCredentials(
        AAD_USER,
        AAD_PWD,
)

dns_client = DnsManagementClient(
        credentials,
        subscription_id
)

def create_dns(name):
    dns_client.record_sets.create_or_update(
            "ifiduk-dns",
            "onifiduk.com",
            name,
            "CNAME",
            {
                "ttl": 300,
                "cname_record": {
                    "cname": "ifiduk-ch-01.australiasoutheast.cloudapp.azure.com"
                }
            }
    )

def delete_dns(name):
    dns_client.record_sets.delete(
        "ifiduk-dns",
        "onifiduk.com",
        name,
        "CNAME"
    )
