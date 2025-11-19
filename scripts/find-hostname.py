#!/usr/bin/env python3
"""
This script retrieves the hostname of a target host from a Zabbix server 
based on the provided IP address.

Usage:
    The script takes one command-line argument, which is the IP address 
    of the target host. It connects to the Zabbix server using the 
    specified credentials and fetches the hostname associated with the 
    given IP address.

Requirements:
    - The `pyzabbix` library must be installed.
    - The Zabbix server address, username, and password must be defined 
      in the variables `zabbix_server_addr`, `username`, and `password`.

Arguments:
    sys.argv[1]: The IP address of the target host.

Output:
    Prints the hostname of the target host to the standard output.

Example:
    $ python3 find-hostname.py 192.168.1.100
    target-hostname
"""

from pyzabbix import ZabbixAPI
import argparse

# input is inventory_hostname
# Parse command-line arguments
parser = argparse.ArgumentParser(description="Retrieve hostname from Zabbix server based on IP address.")
parser.add_argument("-s", "--zabbix-server-addr", required=True, help="Zabbix server address (URL).")
parser.add_argument("-u", "--username", required=True, help="Zabbix server username.")
parser.add_argument("-p", "--password", required=True, help="Zabbix server password.")
parser.add_argument("-i", "--ip_address", required=True, help="IP address of the target host.")
args = parser.parse_args()


# Connect to Zabbix server
zc = ZabbixAPI(url=args.zabbix_server_addr, user=args.username, password=args.password)
res = zc.host.get(filter = {'ip': args.ip_address})
print(res[0]['host'])
