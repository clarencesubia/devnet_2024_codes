#!/usr/bin/env python3

from netmiko import ConnectHandler

# Define Login Credentials
username = 'cisco'
password = 'cisco123'


def configure_device(device_params, config_commands):
    """
    Connect to a device and apply configuration commands.

    :param device_params: Dictionary containing device connection parameters
    :param config_commands: List of commands to configure the device
    """
    print(f"Connecting to {device_params['ip']}...")
    with ConnectHandler(**device_params) as connection:
        print(f"Configuring {device_params['ip']}...")
        output = connection.send_config_set(config_commands)
        print(output)
    print(f"Configuration of {device_params['ip']} completed.\n")


def main():
    # Device configuration parameters
    devices = {
        'R1': {
            'device_type': 'cisco_ios',
            'ip': '192.168.31.101',
            'username': username,
            'password': password,
        },
        'R2': {
            'device_type': 'cisco_ios',
            'ip': '192.168.31.102',
            'username': username,
            'password': password,
        },
        'R3': {
            'device_type': 'cisco_ios',
            'ip': '192.168.31.103',
            'username': username,
            'password': password,
        }
    }

    # Configuration commands for each device
    config_commands = {
        'R1': [
            'interface Loopback0',
            'ip address 192.168.255.1 255.255.255.255',
            'interface g0/2',
            'ip address 10.1.2.1 255.255.255.0',
            'interface g0/3',
            'ip address 10.1.3.1 255.255.255.0',
            'router ospf 1',
            'network 0.0.0.0 255.255.255.255 area 0'
        ],
        'R2': [
            'interface Loopback0',
            'ip address 192.168.255.2 255.255.255.255',
            'interface g0/2',
            'ip address 10.1.2.2 255.255.255.0',
            'interface g0/3',
            'ip address 10.2.3.2 255.255.255.0',
            'router ospf 1',
            'network 0.0.0.0 255.255.255.255 area 0'
        ],
        'R3': [
            'interface Loopback0',
            'ip address 192.168.255.3 255.255.255.255',
            'interface g0/2',
            'ip address 10.1.3.3 255.255.255.0',
            'interface g0/3',
            'ip address 10.2.3.3 255.255.255.0',
            'router ospf 1',
            'network 0.0.0.0 255.255.255.255 area 0'
        ]
    }

    # Apply configurations to devices
    for device_name, device_params in devices.items():
        # print(device_name, device_params)
        configure_device(device_params, config_commands[device_name])

if __name__ == '__main__':
    main()