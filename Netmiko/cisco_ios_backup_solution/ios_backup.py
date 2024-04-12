#!/usr/bin/env python3

from netmiko import ConnectHandler

username = "cisco"
password = "cisco123"

host_ip_addresses = ["192.168.31.101", "192.168.31.102", "192.168.31.103"]

target_hosts = []
for host in host_ip_addresses:
    target_hosts.append(
		{
			"device_type": "cisco_ios",
			"host": host,
			"username": username,
			"password": password
		}
	)

command = "show run"
for target in target_hosts:
	with ConnectHandler(**target) as net_connect:
		output = net_connect.send_command(command)
		
		with open(f"./backups/{target['host']}.txt", "w") as f:
			f.write(output)