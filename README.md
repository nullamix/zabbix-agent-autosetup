# zabbix-agent-autosetup

Automated offline installation and configuration of Zabbix Agent in fully offline (air‑gapped) infrastructures using Ansible.

This repository contains Ansible playbooks and helper scripts to build an offline package bundle (deb and related files), transfer it into an air‑gapped environment, and install and configure the Zabbix agent on target hosts without direct internet access.

## Goals

- Enable reliable installation of Zabbix Agent on hosts with no internet connectivity.
- Provide repeatable, idempotent Ansible playbooks to install packages, drop configuration, and ensure the agent is running.
- Support common Ubuntu targets (and extendable to other distributions).

## Features

- Ansible playbooks to deploy the agent package(s) and apply configuration.
- Variable-driven configuration (Zabbix server address, agent settings).
- Compatibility tested up to Zabbix 5.4 (see Compatibility section).

## Compatibility

This project has been tested on Ubuntu-based distributions and with Zabbix up to version 5.4.

## Requirements

- A "control" machine where you will:
  - Have Ansible installed (with access to package repositories).
- Download the Zabbix agent package for your target OS and rename it according to the name specified in `vars.yml`.
  - Place the renamed package in the `agents` directory.
  - Add any required `userparameters` files to the `userparameters` directory.
- Target hosts in the air-gapped environment with:
  - SSH access from the Ansible control host (with access to package repositories).
  - A supported OS (Ubuntu).
- Tools to transfer the bundle into the air‑gapped environment.

## Quickstart

1. Clone this repository on your online control machine:
   - git clone https://github.com/nullamix/zabbix-agent-autosetup.git


   - The bundle should contain:
     - Zabbix agent package(s) for your target OS (deb)
     - Ansible playbooks for installation

2. Transfer the produced bundle into the air‑gapped environment

3. Place the bundle on a machine in the air-gapped environment that will act as the Ansible control host (or unpack on that machine).

4. Run the Ansible playbook to install and configure the agent:
   - Example:
     - ansible-playbook -i inventory/hosts.ini configure-agent.yml"

## Variables

Store common variables in vars.yml.

## How it works (high level)

- On the offline control machine (inside the air-gapped environment):
  - Installs local package files (dpkg -i / apt install ./*).
  - Places the agent configuration (zabbix_agentd.conf) using templates/variables.
  - Optionally registers the host with a template or monitoring specifics if applicable.

## Contributing

Contributions are welcome. Please:
- Open issues to report bugs or request features.
- Send pull requests for improvements; include tests or verification steps for offline workflows.

## License

This repository is provided under the MIT License. See LICENSE for details.
