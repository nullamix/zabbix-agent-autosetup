#!/usr/bin/env bash

# input is zabbix serever/proxy ip
ZBX_IP=$1
IPs=`traceroute $ZBX_IP | awk {'print $2'} | tail -n +2 | grep -v gate`
echo $IPs | sed 's/ /,/g'
