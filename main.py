from pathlib import Path
import logging
import os
import yaml
from dotenv import load_dotenv

from modules.connection import connection_check
from modules.backup import connect_multiple_info
from modules.configuration import napalm_configure
from modules.verification import verify_configuration


# =========================
# Load credentials
# =========================

load_dotenv()

USERNAME = os.getenv("NET_USERNAME")
PASSWORD = os.getenv("NET_PASSWORD")


# =========================
# Load device inventory
# =========================

with open("devices.yaml", "r") as file:
    inventory = yaml.safe_load(file)

routers = inventory["routers"]

for router in routers:
    router["username"] = USERNAME
    router["password"] = PASSWORD



# Commands for backup

commands = [
    "show version",
    "show ip interface brief",
    "show ip route",
    "show running-config",
    "show running-config | section interface GigabitEthernet0/1"
]



# NAPALM configuration


config = """
interface GigabitEthernet0/1
 description NAPALM_Automation_Test
"""



# Create backup directory


Path("backups").mkdir(exist_ok=True)



# Logging

logging.basicConfig(
    filename="network_automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.getLogger("paramiko").setLevel(logging.WARNING)
logging.getLogger("netmiko").setLevel(logging.WARNING)


#main loop

for router in routers:

    if connection_check(router):

        # 1. Backup
        connect_multiple_info(
            router,
            commands
        )

        # 2. Configure
        napalm_configure(
            router,
            config
        )

        # 3. Verify
        verify_configuration(
            router
        )