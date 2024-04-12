#!/usr/bin/env python3

from netmiko import ConnectHandler
from jinja2 import Template

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


ssh_config = """
username {{ username }} privilege 15 secret {{ secret }}
"""

ssh_template = Template(ssh_config)
ssh_render = ssh_template.render(
	username = "clarence.subia",
	secret = "pass123!"
)

config_set = [ssh_render]
for target in target_hosts:
	with ConnectHandler(**target) as net_connect:
		output = net_connect.send_config_set(config_set)
		print(output)
