#!/usr/bin/env python

from netmiko import ConnectHandler

iosv_l2_s1 = {
	'device_type': 'cisco_ios',
	'ip': '10.0.0.2',
	'username': 'Test',
	'password': 'test',
    'secret': 'test'
}

iosv_l2_s2 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.10.164',
	'username': 'admin',
	'password': 'cisco',
}

with open('ConfigCommands.txt') as f:
	lines = f.read().splitlines()
print(lines)

all_devices = [iosv_l2_s2]

for devices in all_devices:
	net_connect = ConnectHandler(**devices)
	output = net_connect.send_config_set(lines)
	print(output)
