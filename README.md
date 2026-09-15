# Multi-Device Network Automation Tool

A Python-based network automation tool for managing multiple Cisco IOS routers using Netmiko and NAPALM.

## Features

- Multi-device connectivity checks
- Automated device information collection
- Running configuration backups
- NAPALM-based configuration deployment
- Configuration diff before deployment
- Idempotent configuration changes
- Post-change configuration verification
- Centralized logging
- YAML-based device inventory
- Environment-variable-based credential management

## Technologies

- Python
- Netmiko
- NAPALM
- Paramiko
- PyYAML
- python-dotenv
- Git/GitHub
- Cisco IOS
- EVE-NG

## Project Structure
multi-device-network-automation-tool/
│
├── backups/
├── modules/
│   ├── __init__.py
│   ├── backup.py
│   ├── configuration.py
│   ├── connection.py
│   └── verification.py
│
├── .env
├── .gitignore
├── devices.yaml
├── main.py
├── requirements.txt
└── network_automation.log
